import gspread
import time
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Answer
from .serializer import (
    AnswerSerializer,
    ChatMessageSerializer,
    MessageSerializer,
    QuestionChatSerializer,
)

# Create your views here.

answers = [
    {Answer(id=999, vol_id="0", answer="-")},
]

sa = gspread.service_account()
sdb = sa.open("Soft_DB")
userChat = sdb.worksheet("User->chat")
questionChat = sdb.worksheet("Question->chat")
allMessages = sdb.worksheet("All_messages")


def front(request):
    context = {}
    return render(request, "index.html", context)


# Updating the chat
@api_view(["GET", "POST"])
def send_message(request):
    if request.method == "GET":
        get_answers()
        if len(answers) > 1:
            ans = answers[1]
            answers.pop(1)
            serializer = AnswerSerializer(ans, many=True)
            return Response(serializer.data)
        ans = answers[0]
        serializer = AnswerSerializer(ans, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MessageSerializer(data=request.data)
        chat_id = request.query_params.get("chat_id")
        print(request.data)
        if serializer.is_valid():
            f = open("./file.txt", "w")
            f.write(serializer.validated_data["user_id"] + "\n")
            f.write(serializer.validated_data["question"])
            f.close()
            add_message_to_db(
                chat_id,
                serializer.validated_data["user_id"],
                serializer.validated_data["question"],
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Getting all messages from the FAQOption chat
@api_view(["GET"])
def get_question_case(request):
    ind = request.query_params.get("id")
    if ind != 0:
        data = get_chat(ind)
        return Response(data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_faq(request):
    data = get_faqs()
    print(data)
    return Response(data)


def get_answers():
    f = open("answer.txt", "r")
    ans = f.readline()
    f.close()
    if ans != "":
        add_message_to_db(2, 120, ans)
        answers.append({Answer(id=len(answers) + 1, vol_id="120", answer=ans)})
    open("answer.txt", "w").close()
    print(answers)


def add_message_to_db(chat_id, from_id, text):
    allMessages.add_rows(1)
    records = allMessages.get_all_values()
    time.sleep(3)
    index = allMessages.row_count + 1
    print('index: ' + str(index) + ' text:' + text)
    allMessages.update_cell(index, 1, str(chat_id))
    allMessages.update_cell(index, 2, str(from_id))
    allMessages.update_cell(index, 3, str(text))
    print('ADDED')


def verify_user(user_mail):
    records = userChat.get_all_records()
    for record in records:
        if record["user_mail"] == user_mail:
            return record["user_id"]


def get_chat(chat_id):
    records = allMessages.get_all_records()
    chat = filter(lambda record: str(record["chat_id"]) == str(chat_id), records)
    chat = list(chat)
    serializer = ChatMessageSerializer(data=chat, many=True)
    if serializer.is_valid():
        return serializer.validated_data


def get_faqs():
    records = questionChat.get_all_records()
    records = list(records)
    serializer = QuestionChatSerializer(data=records, many=True)
    if serializer.is_valid():
        return serializer.validated_data

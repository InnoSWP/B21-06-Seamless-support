import gspread
import time
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Database.database import Database
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

sdb = Database()


def front(request):
    context = {}
    return render(request, "index.html", context)


# Updating the chat
@api_view(["GET", "POST"])
def send_message(request):
    if request.method == "GET":
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
            sdb.add_message_to_db(
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
        data = sdb.get_chat(ind)
        serializer = ChatMessageSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response(serializer.validated_data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_faq(request):
    data = sdb.get_faqs()
    serializer = QuestionChatSerializer(data=data, many=True)
    if serializer.is_valid():
        return Response(serializer.validated_data)


def get_answers(vol_id, text):
    ans = text
    sdb.add_message_to_db(-99, vol_id, ans)
    answers.append({Answer(id=len(answers) + 1, vol_id="120", answer=ans)})
    print(answers)


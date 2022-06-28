from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Answer
from .serializer import AnswerSerializer, MessageSerializer

# Create your views here.

answers = [
    {Answer(id=999, vol_id="0", answer="-")},
]


def front(request):
    context = {}
    return render(request, "index.html", context)


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
        if serializer.is_valid():
            f = open("./file.txt", "w")
            f.write(serializer.validated_data["user_id"] + "\n")
            f.write(serializer.validated_data["question"])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_answers():
    f = open("./answer.txt", "r")
    ans = f.readline()
    if ans != "":
        answers.append({Answer(id=len(answers) + 1, vol_id="120", answer=ans)})
    f.close()
    open("./answer.txt", "w").close()
    print(answers)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MessageSerializer
from .serializer import AnswerSerializer
from .models import Message
from .models import Answer
from .telegram_bot import bot_message


# Create your views here.


def front(request):
    context = {}
    return render(request, "index.html", context)


answers = [

]
questions = [

]


@api_view(['GET', 'POST'])
def send_message(request):
    if request.method == 'GET':
        print(len(answers))
        if len(answers) > 0:
            ans = answers[0]
            answers.pop(0)
            serializer = AnswerSerializer(ans, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data, many=False)
        print(request.data)
        print(serializer)
        questions.append(request.data)
        print(questions[0]["question"])
        if serializer.is_valid():
            serializer.save()
            if len(questions) > 0:
                bot_message(questions[0]["question"])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

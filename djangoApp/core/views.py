from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MessageSerializer
from .serializer import AnswerSerializer
from .models import Message
from .models import Answer


# Create your views here.


def front(request):
    context = {}
    return render(request, "index.html", context)


answers = [
    {
        Answer(id='120', answer='Yes.')
    },
    {
        Answer(id='120', answer='Tomorrow.')
    },
]


@api_view(['GET'])
def send_message(request):
    if answers.count() != 0:
        ans = answers[0]
        answers.pop(0)
        serializer = AnswerSerializer(ans, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def receive_message(request):
    serializer = AnswerSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
    answers.append(serializer.data)
    receive_message()

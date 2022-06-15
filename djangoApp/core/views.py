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


@api_view(['GET', 'POST'])
def receive_message(request):

    if request.method == 'GET':
        if answers.count() != 0:
            ans = answers[0]
            answers.pop(0)
            serializer = AnswerSerializer(ans, many=False)
            return Response(serializer.data)

    elif request.method == 'POST':
        answers.append(request.data)

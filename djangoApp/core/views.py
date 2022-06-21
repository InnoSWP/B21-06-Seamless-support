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
        Answer(id=999, vol_id='0', answer='-')
    },
    {
        Answer(id=1, vol_id='120', answer='Yes.')
    },
    {
        Answer(id=2, vol_id='120', answer='Tomorrow.')
    },
    {
        Answer(id=3, vol_id='120', answer='Ya spat!')
    },
]


@api_view(['GET', 'POST'])
def send_message(request):
    if request.method == 'GET':
        if len(answers) > 1:
            ans = answers[1]
            answers.pop(1)
            serializer = AnswerSerializer(ans, many=True)
            return Response(serializer.data)
        ans = answers[0]
        serializer = AnswerSerializer(ans, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            f = open('file.txt', 'w')
            f.write(serializer.validated_data['user_id'] + '\n')
            f.write(serializer.validated_data['question'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


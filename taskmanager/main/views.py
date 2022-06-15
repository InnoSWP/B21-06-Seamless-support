import asyncio

from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse, HttpRequest




def index(request):
    return render(request, "main/index.html")


def dialog(request):
    message = request.GET['question']
    user = request.GET['user']
    f = open("text.txt", "w")
    f.write(user+'\n')
    f.write(message)
    f.close()
    return render(request, "main/dialog.html", {'message': message, 'user': user})



def home(request):
    return render(request, "main/form.html", {'message': 'Hello Ernest'})



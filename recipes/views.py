from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Essa é minha home')


def sobre(request):
    return HttpResponse('Esse é meu sobre')


def contato(request):
    return HttpResponse('Essa é meu contatos')

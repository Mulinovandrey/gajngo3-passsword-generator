from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefjhijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFJHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special_char'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(request.GET.get('lenght', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})

def author(request):
    return render(request, 'generator/author.html')

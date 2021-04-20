from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(req):
    return render(req, "generator/home.html",)

def password(req):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if req.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if req.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if req.GET.get('special'):
        characters.extend(list('!~@#$$%^&*()_+-={[}]:;?><,./\\|'))

    length = int(req.GET.get('length', 12))
    thePassword = ""

    for x in range(length):
        thePassword += random.choice(characters)

    return render(req, "generator/password.html", {'password': thePassword})

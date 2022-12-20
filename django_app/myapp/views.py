from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello ji</h1><a href='./about'>About</a>")


def about(request):
    return render(request, "about.html")

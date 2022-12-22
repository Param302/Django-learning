from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello ji</h1><a href='./about'>About</a>")


def about(request):
    person_name = 'hasbulla'
    return render(request, "about.html" , {"name" : person_name})


def form(request):
    try:
        words = request.POST["usertext"]
        return render(request, "form.html", {"text": words, "word_count": len(words.split())})
    except Exception:
        return render(request, "form.html")

def counter(request):
    words = request.POST["usertext"]
    return render(request, "counter.html", {"word_count": len(words.split())})
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import Student

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello ji</h1><a href='./about'>About</a><br/></h1><p>Wanna check Student details ? Click <a href='./details'>here</a>")


def about(request):
    person_name = 'hasbulla'
    return render(request, "about.html" , {"name" : person_name})


def form(request):
    try:
        words = request.POST["usertext"]
        return render(request, "form.html", {"text": words, "word_count": len(words.split())})
    except MultiValueDictKeyError:
        return render(request, "form.html")

def counter(request):
    try:
        words = request.POST["usertext"]
        return render(request, "counter.html", {"word_count": len(words.split())})
    except MultiValueDictKeyError:
        return render(request, "counter.html")


def student_details(request):
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, "details.html", {"students": students, "count": count})
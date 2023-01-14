from .models import Student
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello ji</h1><a href='./about'>About</a><br/><p>Wanna check Student details ? Click <a href='./details'>here</a><br/><p>Sign up <a href='./register'>here</a>")


def about(request):
    person_name = 'hasbulla'
    return render(request, "about.html" , {"name" : person_name})


def form(request):
    if request.method == "POST":
        words = request.POST["usertext"]
        return render(request, "form.html", {"text": words, "word_count": len(words.split())})
    
    return render(request, "form.html")

def counter(request):
    if request.method == "POST":
        words = request.POST["usertext"]
        return render(request, "counter.html", {"word_count": len(words.split())})

    return render(request, "counter.html")


def student_details(request):
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, "details.html", {"students": students, "count": count})

def register(request):
    if request.method != "POST":
        return render(request, "register.html")

    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["pswd"]
    rep_pswd = request.POST["rep-pswd"]
    first = request.POST["first-name"]
    last = request.POST["last-name"]
    # sex = request.POST["sex"]     # doesn't working rn

    if password != rep_pswd:
        messages.error(request, "Password doesn't match!")
        return redirect("register")
    
    user_exists = User.objects.filter(username=username).exists()
    email_exists = User.objects.filter(email=email).exists()
    if user_exists and email_exists:
        messages.error(request, "Username and Email has already been registered!")
        return redirect("register")
    elif user_exists:
        messages.error(request, "Username already exists!")
        return redirect("register")
    elif email_exists:
        messages.error(request, "Email already exists!")
        return redirect("register")
    
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first, last_name=last)
    user.save()
    return redirect("login")
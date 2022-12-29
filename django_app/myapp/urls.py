from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("about", views.about, name="about"),
    path("form", views.form, name="form"),
    path("counter", views.counter, name="counter"),
    path("details", views.student_details, name="student_details"),
]
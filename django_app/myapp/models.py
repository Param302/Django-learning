from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.PositiveSmallIntegerField("Roll no.")
    name = models.CharField("Name", max_length=20)
    cls = models.CharField("Class", max_length=2)
    total_marks = models.PositiveSmallIntegerField("Total marks")
    is_pass = models.BooleanField("Pass?", default=True)

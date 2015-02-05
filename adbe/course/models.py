from django.db import models

# Create your models here.
from adbe.settings import SEMESTER


class Specialty(models.Model):
    name = models.CharField(max_length=255)


class Course(models.Model):
    name = models.CharField(max_length=255)


class Membership(models.Model):
    course = models.ForeignKey(Course)
    specialty = models.ForeignKey(Specialty)
    semester = models.IntegerField(choices=SEMESTER)

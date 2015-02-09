from django.db import models
from django.contrib.auth.models import User

from adbe.course.models import Specialty
from adbe.settings import SEMESTER


class Student(models.Model):
    user = models.OneToOneField(User, unique=True)
    specialty = models.ForeignKey(Specialty)
    semester = models.IntegerField(choices=SEMESTER)

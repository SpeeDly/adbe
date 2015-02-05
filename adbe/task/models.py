from django.db import models

from adbe.course.models import Course
from adbe.lector.models import Lector
from adbe.settings import SEMESTER


class Task(models.Model):
    lector = models.ForeignKey(Lector)
    course = models.ForeignKey(Course)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    expire = models.DateTimeField(auto_now=False, auto_now_add=False)

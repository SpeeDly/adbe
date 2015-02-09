from django.db import models
from django.contrib.auth.models import User
from adbe.course.models import Specialty, Course
from adbe.settings import RESOUCE_PATH, SEMESTER


def path_handler(instance, filename):
    """Set the file name dinamically."""
    return RESOUCE_PATH.format(instance.lector.user.name, filename)


class Lector(models.Model):
    user = models.OneToOneField(User, unique=True)


class Lecture(models.Model):
    lector = models.ForeignKey(Lector)
    course = models.ForeignKey(Course)
    path = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=255)


class LectorCourse(models.Model):
    lector = models.ForeignKey(Lector)
    course = models.ForeignKey(Course)
    approver = models.ForeignKey(Lector, related_name="approver", blank=True, null=True)
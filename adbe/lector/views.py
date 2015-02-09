import os
import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

from adbe.lector.forms import NewLectorForm
from adbe.lector.models import Lector, LectorCourse, Lecture

from adbe.task.models import Task

from adbe.course.models import Specialty, Course
from adbe.course.forms import NewCourseForm
from adbe.settings import SEMESTER, MEDIA_URL, MEDIA_ROOT
# Create your views here.

def signup(request):
    if request.method == "POST":

        form = NewLectorForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            form.save()
            user = authenticate(email=data['email'], password=data['password'])
            auth_login(request, user)
            return redirect("lector_profile")
    else:
        form = NewLectorForm()

    return render(request, 'lector/signup.html', {'form': form})


def profile(request):
    lector = Lector.objects.get(user_id=request.user.id)
    specialties = Specialty.objects.all()
    courses = LectorCourse.objects.exclude(approver__isnull=True).filter(lector=lector)
    courses = [c.course for c in courses]
    courseForm = NewCourseForm()
    tasks = Task.objects.filter(lector=lector).order_by("-created")
    requests = LectorCourse.objects.exclude(lector=lector).filter(course__in=courses, approver__isnull=True)
    return render(request, 'lector/profile.html', {
        "lector": lector, 
        "specialties": specialties, 
        "courses": courses,
        "tasks": tasks,
        "semesters": list(SEMESTER),
        "courseForm": courseForm,
        "requests": list(requests)
        })


def upload(request):
    lector = request.user.lector
    files = request.FILES.getlist("file")
    course = Course.objects.get(id=request.POST.get("course"))

    for f in files:
        path = "{0}/{1}/{2}".format(lector.id, course.id, f.name.replace(" ", "_"))
        default_storage.save(path, ContentFile(f.read()))
        Lecture.objects.create(lector=lector, course=course, path=path, name=f.name, size=f.size)

    return redirect("lector_profile")


def delete(request):
    path = request.GET.get("path")
    default_storage.delete(path)
    Lecture.objects.get(path=path).delete()

    return HttpResponse(json.dumps("COMPLETE"), content_type="application/json")

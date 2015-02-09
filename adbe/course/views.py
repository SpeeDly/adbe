import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from adbe.course.models import Course
from adbe.lector.models import LectorCourse, Lecture
from adbe.course.forms import NewCourseForm
# Create your views here.

def create(request):
    if request.method == "POST":
        lector = request.user.lector
        courseForm = NewCourseForm(request.POST)

        if courseForm.is_valid():
            courseForm.cleaned_data
            course, created = courseForm.save()
            if created:
                LectorCourse.objects.create(
                    course=course,
                    lector=lector,
                    approver=lector
                )
            else:
                LectorCourse.objects.create(
                    course=course,
                    lector=request.user.lector
                )

    return redirect("lector_profile")

def get_uploaded_files(request, id):
    lecture = Lecture.objects.select_related().filter(course_id=id)
    lectures = []
    for l in lecture:
        temp = {
            "name": l.name,
            "created": l.created.strftime("%A %d. %B %Y"),
            "path": l.path,
            "couse_name": l.course.name,
            "size": l.size,
            "uploaded_by": "{0} {1}".format(l.lector.user.first_name, l.lector.user.last_name)
        }
        lectures.append(temp)
    return HttpResponse(json.dumps(lectures), content_type="application/json")

def check_name(request):
    if request.method == "GET":
        response = {}
        name = request.GET.get("course_name")
        count = Course.objects.filter(name=name).count()
        if count:
            response["isExist"] = True
        else:
            response["isExist"] = False

    return HttpResponse(json.dumps(response), content_type="application/json")

def approve(request, id):
    lector = request.user.lector
    lector_course = LectorCourse.objects.filter(id=id).update(approver=lector)
    return redirect("lector_profile")

def reject(request, id):
    lector_course = LectorCourse.objects.get(id=id).delete()
    return redirect("lector_profile")
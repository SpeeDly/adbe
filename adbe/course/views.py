import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from adbe.course.models import Course
from adbe.lector.models import LectorCourse, Lecture
from adbe.course.forms import NewCourseForm
# Create your views here.

def create(request):
    if request.method == "POST":

        courseForm = NewCourseForm(request.POST)

        if courseForm.is_valid():
            data = courseForm.cleaned_data
            print(data["specialtyData"])
            course = courseForm.save()
            LectorCourse.objects.create(
                            course = course,
                            lector = request.user.lector
                             )

    return redirect("lector_profile")

def get_uploaded_files(request, id):
    data = {}
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

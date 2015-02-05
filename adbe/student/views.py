from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from adbe.student.forms import NewStudentForm
from adbe.student.models import Student
from adbe.course.models import Membership
from adbe.task.models import Task


def signup(request):
    if request.method == "POST":

        form = NewStudentForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            form.save()
            user = authenticate(email=data['email'], password=data['password'])
            auth_login(request, user)
            return redirect("student_profile")
    else:
        form = NewStudentForm()

    return render(request, 'student/signup.html', {'form': form})

def profile(request):
    student = Student.objects.get(user_id=request.user.id)
    courses = Membership.objects.select_related().filter(specialty=student.specialty, semester=student.semester)
    courses = [c.course for c in courses]
    tasks = Task.objects.filter(course__in=courses)
    return render(request, 'student/profile.html', {"student": student,
                                                    "courses": courses,
                                                    "tasks": tasks
                                                    })

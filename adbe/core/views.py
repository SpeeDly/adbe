from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login

from adbe.course.models import Membership
from adbe.task.models import Task
from adbe.core.forms import LoginUserForm


def home(request):
    user = request.user
    if user.is_authenticated():
        try:
            user.student
            return redirect("student_profile")
        except:
            user.lector
            return redirect("lector_profile")
    return render(request, 'core/home.html', {})

def login(request):
    if request.method == "POST":

        form = LoginUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                email=data['email'], password=data['password'])

            if user is not None:
                auth_login(request, user)
                return redirect("student_profile")
    else:
        form = LoginUserForm()

    return render(request, 'core/login.html', { 'form': form })


def logout_user(request):
    logout(request)
    return redirect('/')

def download(request):
    student = request.user.student
    courses = Membership.objects.filter(
        specialty=student.specialty,
        semester=student.semester
        )
    courses = [c.course_id for c in courses]
    try:
        task = Task.objects.filter(course_id__in=courses).order_by('?')[0]
    except:
        task = []
    return render(request, 'core/download.html', { 'task': task })
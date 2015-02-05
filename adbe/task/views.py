import json
from datetime import datetime

from django.shortcuts import render
from adbe.task.models import Task
from django.http import HttpResponse


def create(request):
    data = request.GET
    date_time = "{0} {1}".format(data.get("date"), data.get("time"))
    date = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
    Task.objects.create(
                course_id = data.get("course"),
                lector = request.user.lector,
                description = data.get("description"),
                expire = date
                )
    return HttpResponse(json.dumps("COMPLETE"), content_type="application/json")


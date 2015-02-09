# import os
# import re
# import math
import string
import random
import json
# import shutil
# import base64

# from io import BytesIO
# from PIL import Image

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# from glamazer.core.helpers import get_object_or_None, get_fee
from adbe.course.models import Course, Membership

# from glamazer.listings.models import Listing, Tags, ListingTags
from adbe.settings import SEMESTER


class NewCourseForm(ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput())
    specialtyData = forms.CharField(required=True, widget=forms.HiddenInput())
    class Meta:
        model = Course

    def save(self):

        data = self.cleaned_data
        name = data["name"]
        course, created = Course.objects.get_or_create(name=name)
        data["specialtyData"] = json.loads(data["specialtyData"])
        for d in data["specialtyData"]:
            Membership.objects.get_or_create(
                course = course,
                specialty_id = d["specialty"],
                semester = d["semester"]
                )
        
        return (course, created)
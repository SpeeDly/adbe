# import os
# import re
# import math
import string
import random
# import shutil
# import base64

# from io import BytesIO
# from PIL import Image

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# from glamazer.core.helpers import get_object_or_None, get_fee
from adbe.student.models import Student
from adbe.course.models import Specialty
# from glamazer.listings.models import Listing, Tags, ListingTags
from adbe.settings import SEMESTER


class NewStudentForm(ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    password = forms.CharField(widget=(forms.PasswordInput()))
    confirm_password = forms.CharField(widget=(forms.PasswordInput()))
    specialty = forms.ChoiceField(widget=forms.Select())
    semester = forms.ChoiceField(choices=SEMESTER, widget=forms.Select())

    class Meta:
        model = Student
        fields = ['confirm_password', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(NewStudentForm, self).__init__(*args, **kwargs)
        specialities = Specialty.objects.all()
        
        choices = ((0, 'Избери специалност' ),)
        for specialty in specialities:
            choices = choices + ((specialty.id, specialty.name),)
        self.fields['specialty'].choices = choices


    def clean_email(self):

        email = self.cleaned_data['email']
        check_email = User.objects.filter(email=email)

        if check_email:
            raise forms.ValidationError(
                "A user associated with this email address already exists")

        return email

    def clean_password(self):

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not password == confirm_password:
            raise forms.ValidationError("Password mismatch")

        elif len(password) < 6:
            raise forms.ValidationError("Password is too short (6 symbols)")

        elif password.isalpha() or password.isdigit():
            raise forms.ValidationError("Password should contain at least one alphabetic and one non-alphabetic character")

        return password

    def save(self):

        data = self.cleaned_data
        username = ''.join(random.choice(string.ascii_lowercase + string.digits)for x in range(16))

        new_user = User.objects.create_user(
            username = username,
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password'],
            )

        student = Student.objects.create(
                            user=new_user,
                            specialty_id=data["specialty"],
                            semester=data["semester"],
                            )

        return student

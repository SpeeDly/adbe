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
from adbe.lector.models import Lector
# from glamazer.listings.models import Listing, Tags, ListingTags


class NewLectorForm(ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    password = forms.CharField(widget=(forms.PasswordInput()))
    confirm_password = forms.CharField(widget=(forms.PasswordInput()))

    class Meta:
        model = Lector
        fields = ['confirm_password', ]

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

        lector = Lector.objects.create(user=new_user)

        return lector

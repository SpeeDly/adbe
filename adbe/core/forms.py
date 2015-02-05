from django import forms
from django.contrib.auth import authenticate


class LoginUserForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput())
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(render_value=False))

    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                return self.cleaned_data

        raise forms.ValidationError("Invalid login details")

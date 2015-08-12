from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Owner
from django.forms import ModelForm

class OwnerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Owner
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

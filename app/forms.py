from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Driver
from django.forms import ModelForm

class DriverForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Driver.objects.get(username=username)
        except Driver.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
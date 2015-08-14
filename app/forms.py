from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Owner
from bootstrap3_datepicker.widgets import DatePickerInput

class OwnerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Owner
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class DateForm(forms.Form):
    from_date = forms.DateField(widget=DatePickerInput, label='from')
    to_date = forms.DateField(widget=DatePickerInput, label='to')

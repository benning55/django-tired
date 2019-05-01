import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import dayoff


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DayOffForm(forms.ModelForm):
    class Meta:
        model = dayoff
        exclude = ['approve_status', 'create_by']
        widgets = {
            'reason': forms.Textarea(),
            'type': forms.Select(),
            'date_start': forms.DateInput(),
            'date_end': forms.DateInput()
        }

    def clean(self):
        date = super().clean()

        start = date.get('date_start')
        end = date.get('date_end')

        if start > end:
            raise ValidationError('End date cannot come before start sate')
        elif start < datetime.datetime.now().date():
            raise ValidationError('Please do not fill date past')


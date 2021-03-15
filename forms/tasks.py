from django import forms
from django.forms import ModelForm
from tasks.models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title',]
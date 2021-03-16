from django import forms
from django.forms import ModelForm
from tasks.models import *


class TaskForm(forms.ModelForm):
    # title = forms.CharField(
    #         max_length= 256,
    #         widget=forms.TextInput(attrs={
    #                 'tabindex' : '1',
    #             })
    #     )
    # complete = forms.BooleanField()
    class Meta:
        model = Task
        fields = ['title', 'complete',]

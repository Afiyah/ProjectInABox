from django.contrib.auth.models import User
from django import forms
from .models import Test, StudentAnswer

class TestForm(forms.ModelForm):


    class Meta:
        model = StudentAnswer
        fields =[
            'test',
            'student_name',
            'answer_1',
            'answer_2',
        ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



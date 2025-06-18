# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from .models import Project, Task


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'organization']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=255)

class ProjectForm(forms.ModelForm):
    class Meta:
        model =Project 
        fields=['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ['title', 'description', 'project', 'assigned_to', 'status', 'due_date']

from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title","description","genre","director","cast","release_date","image")
        
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email")
        
from django import forms
from .models import *

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title","description","genre","director","cast","release_date","image")
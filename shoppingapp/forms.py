from shoppingapp import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyImage



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class MyImageForm(forms.ModelForm):
    class Meta:
        model=MyImage
        fields='__all__'




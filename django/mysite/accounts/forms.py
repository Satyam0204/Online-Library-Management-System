from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Book, Review

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    

class AddReview(ModelForm):
    class Meta:
        model=Review
        fields='__all__'


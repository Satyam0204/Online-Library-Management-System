from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Book, Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    

class AddReview(ModelForm):
    class Meta:
        model=Order
        fields=['customer','book', 'Review']


class AddBook(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

from concurrent.futures.process import BrokenProcessPool
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Book, Category, Order, Review

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    

class AddReview(ModelForm):
    class Meta:
        model=Review
        fields=['user','book', 'Review']


class AddBook(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class AddCategory(ModelForm):
    class Meta:
        model= Category
        fields='__all__'

class SearchBook(ModelForm):
    class Meta:
        model=Book
        fields=['name','category']
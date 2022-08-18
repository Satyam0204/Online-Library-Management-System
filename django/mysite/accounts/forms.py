
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Book, Category, Order, Review, customerQuery

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
        exclude=['upvote','downvote']

class AddCategory(ModelForm):
    class Meta:
        model= Category
        fields='__all__'

class SearchOrder(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class Issue(ModelForm):
    class Meta:
        model=Order
        fields=['user','book','status']
class QueryForm(ModelForm):
    class Meta:
        model=customerQuery
        fields='__all__'

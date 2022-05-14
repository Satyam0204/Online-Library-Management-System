import imp
from pathlib import Path
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('customers/',views.customers),
    path('books/',views.books, name='books'),
    path('login/',views.loginpage),
    path('register/',views.registerpage),
]

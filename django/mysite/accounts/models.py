import email
from email.mime import image
from email.policy import default
from operator import truth
from telnetlib import STATUS
from tkinter import CASCADE
from django.contrib.auth.models import User
from unicodedata import category
from django.db import models

# Create your models here.

CATEGORY=(('Thriller','Thriller'),('Horror','Horror'),('Knowledge','Knowlegde'))
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    datecreated=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    
    name=models.CharField(max_length=200, null= True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    author=models.CharField(max_length=200,null=True)
    image=models.ImageField(default='defaultbook.png',null=True,blank=True)
    

    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS=(('Rented','Rented'),('Pending','Pending'),('Cancelled','Cancelled'))
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, max_length=200,null=True)
    book=models.ForeignKey(Book, max_length=200, on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=200, null=True,choices=STATUS)
    datecreated=models.DateTimeField(auto_now_add=True, null=True)
    Review=models.TextField(max_length=500,null=True)
    
    
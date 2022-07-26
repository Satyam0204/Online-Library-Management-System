import email
from email.mime import image
from email.policy import default
from operator import truediv, truth
from telnetlib import STATUS

from django.contrib.auth.models import User
from unicodedata import category
from django.db import models

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    datecreated=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    name=models.CharField(max_length=200, null= True)
    category=models.ManyToManyField(Category,related_name='category')
    author=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True,blank=True)
    language=models.ForeignKey(Language,on_delete=models.CASCADE,null=True,blank=True)
    dimennsions=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(max_length=5000,null=True,blank=True)
    image=models.ImageField(default='defaultbook.png',null=True,blank=True)
    upvote=models.ManyToManyField(User,blank=True,related_name='upvote')
    downvote=models.ManyToManyField(User,blank=True,related_name='downvote')
    

    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(Book, max_length=200, on_delete=models.SET_NULL,null=True)
    Review=models.TextField(max_length=500,null=True)
    datecreated=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.book.name

class Order(models.Model):
    STATUS=(('Rented','Rented'),('Pending','Pending'),('Returned','Returned'))
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    book=models.ForeignKey(Book, max_length=200, on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=200, null=True,choices=STATUS)
    dateordered=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.book.name 

class customerQuery(models.Model):
    emailid=models.EmailField(max_length=200,null=True,blank=True)
    query=models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.emailid



    
    
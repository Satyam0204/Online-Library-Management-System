from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.

def home(request):
    
    return render(request, '/home/satyam/django/mysite/accounts/templates/accounts/home.html')
def customers(request):
    return render(request, '/home/satyam/django/mysite/accounts/templates/accounts/customers.html')
def books(request):

    books=Book.objects.all()
    return render(request, '/home/satyam/django/mysite/accounts/templates/accounts/books.html',{'books':books})

def registerpage(request):
    form= CreateUserForm()
    
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            

    context={'form':form}
    return render(request, '/home/satyam/django/mysite/accounts/templates/accounts/register.html',context)


def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.info(request, "Username OR Password is incorrect")
            

    return render(request, '/home/satyam/django/mysite/accounts/templates/accounts/login.html')
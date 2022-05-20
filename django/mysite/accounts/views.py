from unicodedata import name
from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddReview, CreateUserForm
from .decorators import unauthorizedUsers, allowedUsers
from django.contrib.auth.models import Group
# Create your views here.



def home(request):
    
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
@allowedUsers(['admin'])

def customers(request):
    orders=Order.objects.all
    context={'orders':orders}
    return render(request, 'accounts/customers.html',context)

@login_required(login_url='login')

def books(request):

    books=Book.objects.all()
    review=Review.objects.all()
    return render(request, 'accounts/books.html',{'books':books,'review':review})

def registerpage(request):
    form= CreateUserForm()
    
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group=Group.objects.get(name='customer')            
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('home')

    context={'form':form}
    return render(request, 'accounts/register.html',context)

@unauthorizedUsers
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
            
    context={}
    return render(request, 'accounts/login.html',context)

def logoutpage(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('home')

@login_required(login_url='login')

def createReview(request):
    form=AddReview()
    if request.method == 'POST' :
            print("printing post",request.POST)
            form= AddReview(request.POST)
            if form.is_valid():
                form.save()
                return redirect('books')
    context={'form' : form}
    return render (request,'accounts/review_form.html',context)

def userProfile(request):
    context={}
    return render (request,'accounts/userpage.html',context)





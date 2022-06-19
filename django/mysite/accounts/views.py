from ast import Delete
from unicodedata import name
from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddBook, AddCategory, AddReview, CreateUserForm,Issue
from .decorators import unauthorizedUsers, allowedUsers
from django.contrib.auth.models import Group
from .filters import Bookfilter
from django.urls import reverse
# Create your views here.



def home(request):
    books=Book.objects.all()
    
    myfilter=Bookfilter(request.GET,queryset=books)
    books=myfilter.qs
    context={'books':books,'myfilter':myfilter}
    return render(request, 'accounts/home.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])

def customers(request):
    orders=Order.objects.all()
    context={'orders':orders}
    return render(request, 'accounts/customers.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])

def books(request):

    books=Book.objects.all()
    
    form=AddBook()
    categoryform=AddCategory()
   
    
    if request.method == 'POST' :
            form= AddBook(request.POST)
            if form.is_valid():
                form.save()
                return redirect('books')
    
    if request.method == 'POST' :
            categoryform= AddCategory(request.POST)
            if categoryform.is_valid():
                categoryform.save()
                return redirect('books')
    
    return render(request, 'accounts/books.html',{'books':books, 'form':form, 'categoryform': categoryform})

def registerpage(request):
    form= CreateUserForm()
    
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group=Group.objects.get(name='customer')            
            user.groups.add(group)
            login(request, user)       
            return redirect('home')
        
        
        messages.error(request,"Account was not created !!!")

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

def createReview(request,pk):
    
    book=Book.objects.get(id=pk)
    user=request.user
    form=AddReview(initial={'book':book, 'user':user})
    if request.method == 'POST' :
            form= AddReview(request.POST)
            if form.is_valid():
                
                form.save()
                return redirect('books')
    context={'form' : form, 'book':book, 'user':user }
    return render (request,'accounts/review_form.html',context)

def userProfile(request):
    context={}
    return render (request,'accounts/userpage.html',context)



@login_required(login_url='login')
@allowedUsers(['admin'])

def deleteBook(request,pk):
    book_delete=Book.objects.get(id=pk)
    if request.method=='POST':
        book_delete.delete()
        return redirect('books')
    return render (request,'accounts/delete.html',{'book_delete':book_delete})



def bookSearch(request):
    books=Book.objects.all()
    
    myfilter=Bookfilter(request.GET,queryset=books)
    books=myfilter.qs
    context={'books':books,'myfilter':myfilter}
    return render(request,'accounts/booksearch.html',context)

@login_required(login_url='login')


def reviewPage(request,pk):
    books=Book.objects.get(id=pk)
    reviews=books.review_set.all()
    context={'books':books,'reviews':reviews}
    return render(request,'accounts/reviewpage.html',context)


@login_required(login_url='login')
def bookDetail(request,pk):
    book=Book.objects.get(id=pk)
    user=request.user
    status=('Rented','Rented')
    issue=Issue(initial={'book':book, 'user':user,'status':status})
    if request.method == 'POST' :
        issue= Issue(request.POST)
        if issue.is_valid():
            issue.save()
            return redirect(reverse('bookdetail',args=pk))
            
    status2=('Pending','Pending')
    wishlist=Issue(initial={'book':book, 'user':user,'status':status2})
    if request.method == 'POST' :
        wishlist= Issue(request.POST)
        if wishlist.is_valid():
            wishlist.save()
            return redirect(reverse('bookdetail',args=pk))  
                
            
    context={'book':book,'issue':issue,'wishlist':wishlist}
    return render(request,'accounts/bookdetail.html',context)


@login_required(login_url='login')
def myBooks(request):
    user=request.user
    orders=user.order_set.filter(status='Rented')
    context={'orders':orders}
    return render(request,'accounts/mybooks.html',context)

@login_required(login_url='login')
def myWishlist(request):
    user=request.user
    orders=user.order_set.filter(status='Pending')
    
    context={'orders':orders}
    return render(request,'accounts/mywishlist.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])
def updateOrder(request,pk):
    orders=Order.objects.get(id=pk)
    update=Issue(instance=orders)
    if request.method=="POST":
        update= Issue(request.POST,instance=orders)
        if update.is_valid():
            update.save()
            return redirect('customers')
    context={'update':update,'orders':orders}
    return render(request,'accounts/updateorder.html',context)

def delWish(request,pk):
    order_delete=Order.objects.get(id=pk)
    order_delete.delete()
    return redirect('mywishlist')
    
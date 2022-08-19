




from unicodedata import category
from django.shortcuts import render, redirect  

from django.contrib.auth import authenticate, login, logout

from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddBook, AddCategory, AddReview, CreateUserForm
from .decorators import unauthorizedUsers, allowedUsers
from django.contrib.auth.models import Group
from .filters import  Orderfilter
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.


def main():
    group_customer=Group.objects.get(name='customer')
    customer_users=User.objects.filter(groups=group_customer)
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    context={'customer_users':customer_users,'admin_users':admin_users}
    return render('accounts/main.html',context)

def home(request):
    books=Book.objects.all()
    category=Category.objects.all()
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    # if request.is_ajax():
    #     term=request.GET.get('term')
    #     book=Book.objects.filter(name=term)
    #     response=list(book.values())
    #     print(response)
    #    return JsonResponse(response, safe=False)
    # myfilter=Bookfilter(request.GET,queryset=books)
    # books=myfilter.qs
    context={'books':books,'admin_users':admin_users,'category':category}
    return render(request, 'accounts/home.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])

def customers(request):
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    orders=Order.objects.all().order_by('user','dateordered')
    myfilter=Orderfilter(request.GET,queryset=orders)
    orders=myfilter.qs
    context={'orders':orders,'myfilter':myfilter,'admin_users':admin_users}
    
    return render(request, 'accounts/customers.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])

def books(request):

    books=Book.objects.all()
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    
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
    
    return render(request, 'accounts/books.html',{'books':books, 'form':form, 'categoryform': categoryform,'admin_users':admin_users})

def registerpage(request):
    form= CreateUserForm()
    
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group=Group.objects.get(name='customer')            
            user.groups.add(group)
            if user is not None:
                login(request, user)       
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
        else:
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





@login_required(login_url='login')
@allowedUsers(['admin'])

def deleteBook(request,pk):
    book_delete=Book.objects.get(id=pk)
    book_delete.delete()
    return redirect('books')
 




def filterbook(request):
    books=Book.objects.all()
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    filtered_books=Book.objects.none()
    category=Category.objects.all()
    languages=Language.objects.all()
    filters=[]
    
        

    categorys= request.GET.getlist('category[]')
    filters+=categorys
    for i in categorys:
        category_book=Book.objects.filter(category__name=i)
        filtered_books=filtered_books.union(category_book)


    language= request.GET.getlist('language[]')
    filters+=language
    for i in language:
        language_book=Book.objects.filter(language__name=i)
        filtered_books=filtered_books.union(language_book)

    available= request.GET.get('available')
    filters.append(available)
    if (available=='available'):
        available_book=Book.objects.filter(quantity__gt=0)
        filtered_books=filtered_books.union(available_book)



    upvoted_books=[]
    upvoted= request.GET.get('upvotedbooks')
    filters.append(upvoted)
    if (upvoted=='upvoted'):
        for book in books:
            upvotes=book.upvote.count()
            downvotes=book.downvote.count()
            votes=upvotes-downvotes
            if (votes>0):
                upvoted_books.append(book)
        
        filtered_books=filtered_books.union(upvoted_books)
    books=filtered_books
    if(filters==[None, None]):
        books=Book.objects.all()
    context={'books':books,'admin_users':admin_users,'category':category,'languages':languages,'filters':filters}
    return render(request,'accounts/booksearch.html',context)

def browse(request):
    books=Book.objects.all()
    category=Category.objects.all()
    languages=Language.objects.all()
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    # myfilter=Bookfilter(request.GET,queryset=books)
    # books=myfilter.qs
    # categorys=request.GET.getlist('category')
    # print(categorys)
   

    context={'books':books,'admin_users':admin_users,'category':category,'languages':languages}
    return render(request,'accounts/booksearch.html',context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def booksuggestions(request):
    if is_ajax(request):

        term=request.GET.get('term')
        books=Book.objects.filter(name__icontains=term)
        response_content=list(books.values())
        

        return JsonResponse(response_content,safe=False)
    



def bookSearch(request):
    books=Book.objects.none()
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    id=request.GET.get('name')
    
    books=Book.objects.filter(id=id)
 
    category=Category.objects.all()
    languages=Language.objects.all()
    context={'books':books,'admin_users':admin_users,'category':category,'languages':languages}
    return render(request,'accounts/booksearch.html',context)



@login_required(login_url='login')





@login_required(login_url='login')
def bookDetail(request,pk):
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    book=Book.objects.get(id=pk)
    reviews=book.review_set.all()
    length=len(reviews)
    user=request.user
    uv=book.upvote.all()
    dv=book.downvote.all()
    similar_categories=list(book.category.all())
    similar_books=Book.objects.none()
    for category in similar_categories:

        
        similar_cat_books=Book.objects.filter(category__name=category.name).exclude(name=book.name)
        
        similar_books=similar_books.union(similar_cat_books)

    upvotes=book.upvote.count()
    downvotes=book.downvote.count()
    votes=upvotes-downvotes
    pending=user.order_set.filter(book=book,status='Pending')
    issued=user.order_set.filter(book=book,status='Rented')
    context={'book':book,'similar_books':similar_books,'reviews':reviews,'pending':pending,'issued':issued,'votes':votes,'uv':uv,'dv':dv,'admin_users':admin_users,'length':length}
    return render(request,'accounts/bookdetail.html',context)


@login_required(login_url='login')
def myBooks(request):
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    user=request.user
    orders=user.order_set.filter(status='Rented')
    context={'orders':orders,'admin_users':admin_users}
    return render(request,'accounts/mybooks.html',context)

@login_required(login_url='login')
def myissuereqeuest(request):
    user=request.user
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    orders=user.order_set.filter(status='Pending')
    
    context={'orders':orders,'admin_users':admin_users}
    return render(request,'accounts/myissuerequest.html',context)

@login_required(login_url='login')
@allowedUsers(['admin'])
def saveOrder(request,pk):
    order=Order.objects.get(id=pk)
    order.status=request.POST.get('status')
    q=order.book.quantity
    if request.method=="POST":
        if request.POST.get('status')=='Rented':
            q=q-1
            book=Book.objects.get(name=order.book.name)
            book.quantity=q
            book.save()
        if request.POST.get('status')=='Returned':
            q=q+1
            book=Book.objects.get(name=order.book.name)
            book.quantity=q
            book.save()
        order.save()
        return redirect('home')

@login_required(login_url='login')
@allowedUsers(['admin'])

def updateBook(request,pk):
    book=Book.objects.get(id=pk)
    update=AddBook(instance=book)
    if request.method=="POST":
        update=AddBook(request.POST,instance=book)
        if update.is_valid():
            update.save()
            return redirect('books')
    context={'update':update}
    return render(request,'accounts/updatebook.html',context)

@login_required(login_url='login')
def delWish(request,pk):
    order_delete=Order.objects.get(id=pk)
    order_delete.delete()
    return redirect('myissuerequest')

@login_required(login_url='login')
@allowedUsers(['admin'])
def moderator(request):
    group_admin=Group.objects.get(name='admin')
    admin_users=User.objects.filter(groups=group_admin)
    group_customer=Group.objects.get(name='customer')
    customer_users=User.objects.filter(groups=group_customer)
    context={'admin_users':admin_users,'customer_users':customer_users}
    return render(request,'accounts/moderator.html',context)


@login_required(login_url='login')
@allowedUsers(['admin'])
def addAdmin(request,pk):
    user=User.objects.get(id=pk)
    group_admin=Group.objects.get(name='admin')   
    group_customer=Group.objects.get(name='customer')   
    user.groups.remove(group_customer)
    user.groups.add(group_admin)
    return redirect('moderator')


@login_required(login_url='login')
@allowedUsers(['admin'])
def removeAdmin(request,pk):
    user=User.objects.get(id=pk)
    group_admin=Group.objects.get(name='admin')   
    group_customer=Group.objects.get(name='customer')   
    user.groups.add(group_customer)
    user.groups.remove(group_admin)
    
    return redirect('moderator')


@login_required(login_url='login')
def issuebook(request,pk):

    book=Book.objects.get(id=pk)
    user=request.user
    status='Pending'

    Order.objects.create(book=book,user=user,status=status)
    return redirect(reverse('bookdetail',args=pk))


def upvote(request,pk):
    user=request.user
    book=Book.objects.get(id=pk)
    book.upvote.add(user)
    book.downvote.remove(user)

    return redirect(reverse('bookdetail',args=pk))

def rm_upvote(request,pk):
    user=request.user
    book=Book.objects.get(id=pk)
    book.upvote.remove(user)
    return redirect (reverse('bookdetail',args=pk))
def rm_downvote(request,pk):
    user=request.user
    book=Book.objects.get(id=pk)
    book.downvote.remove(user)
    return redirect (reverse('bookdetail',args=pk))

def downvote(request,pk):
    user=request.user
    book=Book.objects.get(id=pk)
    book.downvote.add(user)
    book.upvote.remove(user)

    return redirect(reverse('bookdetail',args=pk))

def saveQuery(request):
    email=request.POST.get('emailid')
    query=request.POST.get('query')
    customerQuery.objects.create(emailid=email,query=query)
    return redirect('home')

@login_required(login_url='login')
@allowedUsers(['admin'])
def viewQuery(request):
    queries=customerQuery.objects.all()
    context={'queries':queries}

    return render(request,'accounts/queries.html',context)

# def nav(request):
    
#     admin=Group.objects.get(name='admin')
#     admin_users=User.objects.filter(group=admin)
#     customer=Group.objects.get(name='customer')
#     context={'admin_users':admin_users,'customer':customer}
#     return render(request,'accounts/navbar .html',context)

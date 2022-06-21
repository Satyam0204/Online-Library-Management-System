import imp
from pathlib import Path
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('customers/',views.customers,name='customers'),
    path('books/',views.books, name='books'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path('addreview/<str:pk>/',views.createReview,name='addreview'),
    path('userpage/',views.userProfile,name='userpage'),
    path('deletebook/<str:pk>/',views.deleteBook,name='deletebook'),
    path('booksearch/',views.bookSearch,name='booksearch'),
    path('reviewpage/<str:pk>/',views.reviewPage,name='reviewpage'),
    path('bookdetail/<str:pk>/',views.bookDetail,name='bookdetail'),
    path('updateorder/<str:pk>/',views.updateOrder,name='updateorder'),
    path('updatbook/<str:pk>/',views.updateBook,name='updatebook'),
    path('mybooks/',views.myBooks,name='mybooks'),
    path('mywishlist/',views.myWishlist,name='mywishlist'),
    path('delwish/<str:pk>/',views.delWish,name='delwish'),
    path('moderator/',views.moderator,name='moderator'),
    path('addadmin/<str:pk>/',views.addAdmin,name='addadmin'),
    path('removeadmin/<str:pk>/',views.removeAdmin,name='removeadmin'),

]

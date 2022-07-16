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
    path('updatbook/<str:pk>/',views.updateBook,name='updatebook'),
    path('mybooks/',views.myBooks,name='mybooks'),
    path('myissuerequest/',views.myissuereqeuest,name='myissuerequest'),
    path('delwish/<str:pk>/',views.delWish,name='delwish'),
    path('moderator/',views.moderator,name='moderator'),
    path('addadmin/<str:pk>/',views.addAdmin,name='addadmin'),
    path('removeadmin/<str:pk>/',views.removeAdmin,name='removeadmin'),
    path('issuebook/<str:pk>/',views.issuebook,name='issuebook'),
    path('upvote/<str:pk>/',views.upvote,name='upvote'),
    path('removeupvote/<str:pk>/',views.rm_upvote,name='removeupvote'),
    path('downvote/<str:pk>/',views.downvote,name='downvote'),
    path('removedownvote/<str:pk>/',views.rm_downvote,name='removedownvote'),
    path('saveorder/<str:pk>/',views.saveOrder,name='saveorder'),
    path('savequery/',views.saveQuery,name='savequery'),
    path('navbar/',views.nav,name='navbar'),
   


]

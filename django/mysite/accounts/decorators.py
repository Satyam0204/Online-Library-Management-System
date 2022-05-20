from tokenize import group
from urllib import request
from django.shortcuts import redirect
from django.http import HttpResponse

def unauthorizedUsers(view_func):
    def wrap_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args, **kwargs)
    return wrap_func

def allowedUsers(allowed_roles=[]):
    def decorator(view_func):
        def wrap_func(request,*args, **kwargs):

            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("not authorized")
        return wrap_func
    return decorator

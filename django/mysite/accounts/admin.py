from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Review)
admin.site.register(customerQuery)


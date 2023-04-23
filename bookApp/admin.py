from django.contrib import admin


   
# Register your models here.
from .models import Book,Users

admin.site.register(Book)
admin.site.register(Users)
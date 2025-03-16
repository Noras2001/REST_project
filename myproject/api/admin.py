from django.contrib import admin
from . import models
from .models import Book, Category

admin.site.register(Book)
admin.site.register(Category)



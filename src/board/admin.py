from django.contrib import admin

# Register your models here.

from .models import BoardPost

admin.site.register(BoardPost)
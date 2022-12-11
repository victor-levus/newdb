from django.contrib import admin

from . import models

# Register your models here.

    
@admin.register(models.Course )
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    ordering = ['title']
    list_per_page = 15
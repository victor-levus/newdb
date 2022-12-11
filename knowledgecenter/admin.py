from urllib.parse import urlencode
from django.db.models import Count
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from . import models

# Register your models here.

@admin.register(models.Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'student_count']
    ordering = ['-title']
    list_per_page = 15
    search_fields = ['title']


    @admin.display(ordering='student_count')
    def student_count(self, programme):
        url = (reverse('admin:knowledgecenter_student_changelist') 
        + '?'
        + urlencode({
            'programme__id': str(programme.id)
        })
        )
        return format_html('<a href="{}">{}</a>', url, programme.student_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count=Count('student')
            
        )

@admin.register(models.ProgramState)
class ProgramStateAdmin(admin.ModelAdmin):
    list_display = ['title', 'student_count']
    ordering = ['title']
    list_per_page = 15
    search_fields = ['title']


    @admin.display(ordering='student_count')
    def student_count(self, programstate):
        url = (reverse('admin:knowledgecenter_student_changelist') 
        + '?'
        + urlencode({
            'programstate__id': str(programstate.id)
        })
        )
        return format_html('<a href="{}">{}</a>', url, programstate.student_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            student_count=Count('student')
            
        )



@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['programme', 'programstate']
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'gender', 'phone', 'state', 'program_state_name']
    ordering = ['first_name', 'last_name']
    list_per_page = 15
    # list_editable = ['gender']
    list_filter = ['programme__title','programstate__title', 'last_update']
    list_select_related = ['programstate']


    @admin.display(ordering='programstate')
    def program_state_name(self, student):
        return student.programstate.title


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    ordering = ['title']
    list_per_page = 15


@admin.register(models.Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['first_name']
    list_per_page = 15


@admin.register(models.Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'role']
    ordering = ['user__first_name']
    list_per_page = 15



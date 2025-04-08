from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from projects.models.project import Project
from projects.models.project_file import ProjectFile
from projects.models.tag import Tag
from projects.models.task import Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_count_of_files', 'date_started']
    search_fields = ['name']

    def display_count_of_files(self, obj):
        return obj.count_of_files

    display_count_of_files.short_description = 'Count of Files'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'created_at', 'due_date']
    search_fields = ['title']
    list_filter = ['status', 'priority', 'project', 'created_at', 'due_date']

    def change_status(self, request, objects):
        for obj in objects:
            obj.status = 'CLOSED'
            obj.save()
        return objects

    change_status.short_description = 'Mark as Closed'

    actions = ['change_status']


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'position')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'projects', 'birth_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'position')
    search_fields = ('username', 'last_name', 'email')
    list_filter = ('position', 'projects',)
    ordering = ('username',)


admin.site.unregister(Group)
admin.site.register(Group)

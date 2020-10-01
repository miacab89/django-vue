from django.contrib import admin
from task.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'updated_at')
    list_display = ('title', 'description', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)

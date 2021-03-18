from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, Permission
import datetime

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.batch = datetime.date.today()
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
admin.site.register(User)
admin.site.register(Batch)

admin.site.unregister(Group)

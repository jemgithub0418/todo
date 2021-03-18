from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, Permission
import datetime

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        batch = Batch.objects.create(batch = datetime.date.today())
        obj.batch = batch
        super().save_model(request, obj, form, change)

    fieldsets = (
        ('', {'fields': ('title', 'author',)}),
    )
    list_display = ('title', 'author', 'complete', 'batch',)
    list_display_links = ('title', 'author', 'complete', 'batch',)


admin.site.register(Task, TaskAdmin)
admin.site.register(User)
admin.site.register(Batch)

admin.site.unregister(Group)

from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('undo/<int:id>/', views.undotask, name='undo'),
    path('previous-tasks/<str:batch>/', views.batch_details, name = 'batch-details'),
    path('delete/<int:id>/', views.delete_task, name='delete-task'),

]

from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('undo/<int:id>/', views.undotask, name='undo'),
    path('previous-tasks/<int:id>/', views.batch_details, name = 'batch-details'),

]

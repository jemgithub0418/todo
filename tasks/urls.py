from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('undo/<str:id>/', views.undotask, name='undo'),
]

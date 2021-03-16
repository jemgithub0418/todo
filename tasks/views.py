from django.shortcuts import render, redirect
from .models import Task
from forms import tasks
from django.http import JsonResponse


def home(request):
    form = tasks.TaskForm()
    if request.method == 'POST':
        form = tasks.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks:home')
    else:
        form = tasks.TaskForm()
    context = {
        'form' : form,
        'completed_tasks' : Task.objects.filter(complete = True).order_by('-created'),
        'unfinished_tasks' : Task.objects.filter(complete= False).order_by('-created'),
    }
    return render(request, 'tasks/home.html', context)


def undotask(request, id):
    task = Task.objects.get(id = id)
    if request.method  == 'POST':
        if task.complete == True:
            task.complete = False
        else:
            task.complete = True
        task.save()
    return redirect('tasks:home')

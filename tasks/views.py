from django.shortcuts import render, redirect
from .models import Task
from forms import tasks


def home(request):
    form = tasks.TaskForm()
    if request.method == 'POST':
        form = tasks.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid")
        return redirect('tasks:home')
    else:
        print('form not valid')
    context = {
        'form' : form,
        'completed_tasks' : Task.objects.filter(complete = True).order_by('created'),
        'unfinished_tasks' : Task.objects.filter(complete= False).order_by('created'),
    }
    return render(request, 'tasks/home.html', context)

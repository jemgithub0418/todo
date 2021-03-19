from django.shortcuts import render, redirect
from .models import Task, Batch
from forms import tasks
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.formats import date_format


@login_required
def home(request):
    batch = Batch.objects.filter(batch = datetime.date.today()).first()
    if request.method == 'POST':
        form = tasks.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if not batch:
               batch =  Batch.objects.create(batch = datetime.date.today())
            task.author = request.user
            task.batch = batch
            task.save()
        return redirect('tasks:home')
    else:
        form = tasks.TaskForm()
    context = {
        'form' : form,
        'batch_list' : Batch.objects.filter(batch__lt = datetime.date.today()),
        'completed_tasks' : Task.objects.filter(author = request.user,batch__batch = datetime.date.today(), complete = True).order_by('-created'),
        'unfinished_tasks' : Task.objects.filter(author = request.user,batch__batch = datetime.date.today(), complete = False).order_by('-created'),
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


def batch_details(request, batch):
    task_list = Task.objects.filter(author = request.user, batch__batch = batch).order_by('-created')
    batch_list = Batch.objects.filter(batch__lt = datetime.date.today())
    context = {
        'task_list' : task_list,
        'batch_list' : batch_list,
        'specific_batch': Batch.objects.get(batch = batch),
    }
    return render(request, 'tasks/batch_details.html', context)

def delete_task(request, id):
    delete_task = Task.objects.get(id = id)
    delete_task.delete()
    return redirect('tasks:home')

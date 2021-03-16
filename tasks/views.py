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
        print('invalid form')
    context = {
        'form' : form,
        'completed_tasks' : Task.objects.all().order_by('complete', '-created'),
        # 'unfinished_tasks' : list(Task.objects.filter(complete= False).order_by('created')),
    }
    return render(request, 'tasks/home.html', context)


# def updatetask(request):
#     if request.is_ajax() and request.method == "POST":
#         task = Task.objects.get(id = request.task.id)
#         task.complete = True if request.POST.get('task.complete') == 'True' else False
#         task.save()
#         data = { 'status': 'success', 'task.complete': task.complete }
#         return JsonResponse(data, status = 200)
#     else:
#         data = {'status':'error'}
#         return JsonResponse(data, status=400)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    
    return redirect('home')

def deleteTask(request,pk):
    task = get_object_or_404(Task, pk=pk) 
    task.delete()   
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()

    return redirect('home')

def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()

    return redirect('home')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')

    else:
        context = {
            'get_task': get_task,
        }
        return render(request, "edit_task.html", context)
    
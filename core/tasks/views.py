from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import Task
from userauth.models import Profile
# Create your views here.
def addTask(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        print(request.POST)
        form = taskForm(request.POST or None)
        task = Task()
        if form.is_valid():
            task.user = form.cleaned_data['user']
            task.task_title = form.cleaned_data['task_title']
            task.priority = form.cleaned_data['priority']
            task.due_date = form.cleaned_data['due_date']
            task.task_todos = form.cleaned_data['task_todos']
          
            task.save()
            messages.info(request,f'success')
            return redirect('add_task')
        else:
            messages.error(request, f"error")
            return redirect('add_task')
    form = taskForm()
    context = {
        'form':form,
        'tasks':tasks
    }
    return render(request, 'tasks/addTask.html',context)




def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = taskEditForm(request.POST, instance=task)
        task1 = Task()
        if form.is_valid():
            # task1.task_title  = form.cleaned_data['task_title']
            # task1.priority  = form.cleaned_data['priority']
            # task1.due_date = form.cleaned_data['due_date']
            form.save()
            messages.info(request, 'Task Updated Successful')
            return redirect('add_task')
        else:
            messages.error(request, 'Error occured')
            return redirect('update_task', id=id)
    
    form = taskEditForm(instance=task)
    context = {
        'form':form
    }
    return render(request, 'tasks/updateTask.html', context)



def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('profile', id=task.user.profile.id)


def assign_task(request):
    # data = Profile.objects.get(id=id)
    profiles =  Profile.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = assignTaskForm(request.POST)
        task = Task()
        if form.is_valid():
            task.user = form.cleaned_data['user']
            task.task_title = form.cleaned_data['task_title']
            task.priority = form.cleaned_data['priority']
            task.due_date = form.cleaned_data['due_date']
            task.assigned_by = request.user
            task.task_todos = form.cleaned_data['task_todos']
            task.save()
            messages.info(request,f'success')
            return redirect('home')
        else:
            messages.error(request, f"error")
            return redirect('add_task')
    form = assignTaskForm()
    context = {
        "form":form,
        'profiles':profiles
    }
    return render(request ,'tasks/assignTask.html', context)
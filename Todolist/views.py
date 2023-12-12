from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


#### THE LOGICFOR THE DO-TO LIST

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to the database
            return redirect('/')
    else:
        form = TaskForm()  # returns to the same page (to fill the form again)
    return render(request, 'taskform.html', {'form': form})


### Update data, we update the id
# to include an id...
def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
##Save and redirect
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = TaskForm(instance=task)

    return render(request, 'taskform.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')

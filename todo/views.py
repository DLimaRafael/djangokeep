from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task

# Create your views here.
def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'all_tasks':tasks})

def add_todo_view(request):
    x = request.POST['content']
    new_item = Task(content = x)
    new_item.save()
    return HttpResponseRedirect('/')

def mark_done(request, i):
    x = Task.objects.get(id=i)
    is_done : bool = getattr(x, 'is_done')
    setattr(x, 'is_done', not is_done)
    x.save()
    return HttpResponseRedirect('/')

def delete_task(request, i):
    x = Task.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('/')
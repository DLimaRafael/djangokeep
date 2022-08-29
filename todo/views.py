from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Task

# Create your views here.
def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'all_tasks':tasks})

def arch_list(request):
    tasks = Task.objects.filter(is_archived=True)
    return render(request, 'archive.html', {'all_tasks':tasks})

def add_note(request):
    x = request.POST['content']
    # Avoiding addition of empty notes
    if x == '':
        return HttpResponseRedirect('/')
    new_item = Task(content = x)
    new_item.save()
    return HttpResponseRedirect('/')

def archive_note(request, i):
    x = Task.objects.get(id=i)
    is_archived : bool = getattr(x, 'is_archived')
    setattr(x, 'is_archived', not is_archived)
    x.save()
    if is_archived == True:
        return HttpResponseRedirect('/archive/')
    return HttpResponseRedirect('/')

def delete_note(request, i):
    x = Task.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('/')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todolist(request):
    todos = Todo.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()

    return render(request, 'myapp/todolist.html', {'todos': todos, 'form': form})

def toggle_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')

def delete_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('home')

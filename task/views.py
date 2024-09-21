from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Task

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy("task_list")
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")

class TaskCompleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.finished_at = date.today()
        task.save()
        return redirect("task_list")
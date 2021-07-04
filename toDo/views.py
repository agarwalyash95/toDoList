from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from toDoList.settings import TEMPLATES
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = TEMPLATES[0]['DIRS'][0] + '/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        search = self.request.GET.get('searchArea') or ''
        if search:
            context['tasks'] = context['tasks'].filter(title__icontains=search)
        context['search'] = search
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = TEMPLATES[0]['DIRS'][0] + "/listview.html"
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = TEMPLATES[0]['DIRS'][0] + "/AddView.html"
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = TEMPLATES[0]['DIRS'][0] + "/AddView.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = TEMPLATES[0]['DIRS'][0] + "/TaskDelete.html"
    success_url = reverse_lazy('tasks')

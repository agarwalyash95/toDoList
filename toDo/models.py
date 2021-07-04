from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

class TodoGroup(models.Model):
    group = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class GroupUsers(models.Model):
    group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class groupTask(models.Model):
    group = models.ForeignKey(GroupUsers, on_delete=models.CASCADE, null=True, blank=True)
    assignedto = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

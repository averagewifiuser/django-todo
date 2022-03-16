from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, blank=False)
    owner = models.ForeignKey('auth.User', related_name='todolists', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Tasks(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False, default='pending')
    description = models.TextField(blank=True)
    due = models.DateTimeField(default=timezone.now)
    todo = models.ForeignKey(TodoList, related_name='tasks', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']


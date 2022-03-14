from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tasks, TodoList


class TasksSerializer(serializers.ModelSerializer):
    todolist = serializers.ReadOnlyField(source='todo.id')

    class Meta:
        model = Tasks
        fields = ['id', 'name', 'status', 'description', 'due', 'todo']


class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Tasks.objects.all())

    class Meta:
        model = TodoList
        fields = ['id', 'title', 'owner', 'tasks']


class UserSerializer(serializers.ModelSerializer):
    todolists = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoList.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todolists']
        
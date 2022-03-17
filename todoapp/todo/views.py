from .models import Tasks, TodoList
from .serializers import TodoListSerializer, TasksSerializer
from .permissions import IsOwner
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action


class TodoLists(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

        
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        todo_obj = TodoList.objects.get(pk=self.kwargs.get('todo_id'))
        serializer.save(todo=todo_obj)

    @action(detail=True)
    def detail(self, request, *args, **kwargs):
        task = Tasks.objects.get(pk=self.kwargs.get('pk'))
        task_obj = {
            "name": task.name,
            "status": task.status,
            "description": task.description,
            "due": task.due,
            "created": task.created
        }
        return Response(task_obj)
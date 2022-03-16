from .models import Tasks, TodoList
from .serializers import TodoListSerializer, TasksSerializer
from .permissions import IsOwner
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


@api_view(['POST', 'GET'])
def create_task(request):
    '''
    Create a new request
    '''
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


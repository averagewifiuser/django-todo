from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


tasks_view = views.TasksViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tasks_detail = views.TasksViewSet.as_view({
    'get' :'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('todolists/', views.TodoLists.as_view(), name='todolists'),
    path('todolists/<int:pk>/', views.TodoListDetail.as_view(), name='todolist-detail'),
    path('todolists/<int:todo_id>/tasks/', tasks_view, name='tasks'),
    path('todolists/<int:todo_id>/tasks/<int:pk>/', tasks_detail, name='task-detail')

])
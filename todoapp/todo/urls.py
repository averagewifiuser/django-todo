from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('todolists/', views.TodoLists.as_view(), name='todolists'),
    path('todolists/<int:pk>/', views.TodoListDetail.as_view(), name='todolist-detail'),
    path('tasks/', views.create_task, name='create-task'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
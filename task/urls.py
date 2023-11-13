from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('task-assignment/', views.TaskAssignmentView.as_view(), name='task-assignment'),
    path('view-task/', views.ListTaskView.as_view(), name="view-task"),
    path('update-task/<int:pk>/', views.UpdateTaskView.as_view(), name= "update-task"),
    path('delete-task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('task-detail/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('my-task/', views.my_task, name="my-task"),
    path('update-task-status/<int:pk>/', views.UpdateTaskStatusView.as_view(), name = 'update-task-status')
]



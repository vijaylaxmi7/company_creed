from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('task-assignment/', views.TaskAssignment.as_view(), name='task-assignment'),
    # path('send-task/', views.SendTask, name='send task' ),
    path('view-task/', views.viewTask.as_view(), name="view-task"),
    # path('my-task/', views.myTask, name="my-task"),
    path('update-task/<int:pk>/', views.updateTask.as_view(), name= "update-task"),
    path('delete-task/<int:pk>/', views.deleteTask.as_view(), name='delete-task')
]



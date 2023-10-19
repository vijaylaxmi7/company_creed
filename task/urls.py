from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('task-assignment/', views.taskAssignment.as_view(), name='task-assignment')
]



from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('leave-application/', views.LeaveApplication.as_view(), name='leave-application'),
    path('send-mail/', views.send_custom_email, name="send-mail"),

]



from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

     path('check-in/', views.CreateCheckInOutTime.as_view(), name='check-in' ),
     path('check-out/', views.CreateCheckInOutTime.as_view(), name = 'check-out'),
     path('check-in-out/', views.CheckInOutStatus.as_view(), name='check-in-out'),
]



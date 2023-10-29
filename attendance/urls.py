from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

     path('check-in/', views.CreateCheckInTime, name='check-in' ),
     path('check-out/', views.CreateCheckInTime, name = 'check-out'),
     path('check-in-out/', views.CheckInOutStatus.as_view(), name='check-in-out')

]



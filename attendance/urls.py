from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

     path('check-in/', views.CreateCheckInOutTimeView.as_view(), name='check-in' ),
     path('check-out/', views.CreateCheckInOutTimeView.as_view(), name = 'check-out'),
     path('check-in-out/', views.EmployeeCheckInOutView.as_view(), name='check-in-out'),
     path('total-working-hours/', views.EmployeeWorkingHourView.as_view(), name='total-working-hours'),
     path('user-check-in-out/', views.UserCheckInOutView.as_view(), name= 'user-check-in-out'),
     path('user-work-hour/', views.UserWorkHourView.as_view(), name = 'user-work-hour'),
]



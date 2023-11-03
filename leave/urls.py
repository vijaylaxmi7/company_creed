from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('leave-application/', views.LeaveApplication.as_view(), name='leave-application'),
    path('manage-leave/', views.ManageLeaveApplication.as_view(), name="leave-manage"),
    path('status/<int:pk>/', views.updateStatus.as_view(), name="status"),
    path('send-status/<int:employeeleave_id>/', views.LeaveApproveReject, name="send-status")

]



from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('leave-application/', views.LeaveApplication.as_view(), name='leave-application'),
    path('manage-leave/', views.ManageLeaveApplication.as_view(), name="leave-manage"),
    path('leave-approve-reject/<int:id>/', views.LeaveApproveReject, name="leave-approve-reject"),
    path('leave-balance/', views.LeaveBalanceView, name='leave-balance'),
    path('my-leave/', views.MyLeave.as_view(), name='my-leave')

]



from django.urls import path
from . import views




urlpatterns = [

    path('leave-application/', views.LeaveApplication.as_view(), name='leave-application'),
    path('manage-leave/', views.ManageLeaveApplication.as_view(), name="leave-manage"),
    path('leave-approve-reject/<int:id>/', views.LeaveApproveRejectView.as_view(), name="leave-approve-reject"),
    path('leave-balance/', views.LeaveBalanceView, name='leave-balance'),
    path('my-leave/', views.MyLeave.as_view(), name='my-leave'),

]



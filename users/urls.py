from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("signup/", views.EmployeeSignupForm.as_view(), name="user signup form"),
    path('signin/',views.EmployeeSignin.as_view(), name='user signin form'),
    path('logout/', views.Logout, name = 'logout'),
    path('send_mail/', views.SendMail, name='send mail'),
    path('reset_password/', views.resetPasswordView.as_view(), name= "reset_password"),
    path('change_password/<token>/', views.changePassword, name= "change_password"),
    path('forget_password/', views.ForgetPassword, name='forget_password')
]
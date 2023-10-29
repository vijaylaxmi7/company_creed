from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



urlpatterns = [

    path("signup/", views.EmployeeSignupForm.as_view(), name="user-signup"),
    path('signin/',views.EmployeeSignin.as_view(), name='user signin form'),
    path('logout/', views.Logout, name = 'logout'),
    path('index/', views.index, name =  'index'),
    path('home/', views.home, name =  'home'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(), name='change_password_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset_form.html' ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
    path('edit-profile/<int:pk>/', views.EditProfileView.as_view(), name= "edit-profile"),
    path('my-task/', views.myTask, name="my-task")


    # path('send_mail/', views.SendMail, name='send mail'),
    # path('reset_password/', views.resetPasswordView.as_view(), name= "reset_password"),
    # path('change_password/<token>/', views.changePassword, name= "change_password"),
    # path('forget_password/', views.ForgetPassword, name='forget_password'),
    # path('',TemplateView.as_view(template_name="users/password_reset_confirm.html"),
        # name='password_reset_confirm'),

]

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



urlpatterns = [

    path("signup/", views.EmployeeSignupView.as_view(), name="user-signup"),
    path('signin/',views.EmployeeSigninView.as_view(), name='user-signin'),
    path('logout/', views.Logout, name = 'logout'),
    path('index/', views.index, name =  'index'),
    path('edit-profile/<int:pk>/', views.EditProfileView.as_view(), name= "edit-profile"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset_form.html' ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
    
]

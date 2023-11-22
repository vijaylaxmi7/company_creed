from django.urls import path
from . import views

urlpatterns = [

    path('generate-salary-slip/<int:id>/', views.GenerateSalarySlip.as_view(), name= "generate-salary-slip"),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee-list'),
    path('download-salary-slip/<int:id>/',views.DownloadSalarySlipView.as_view(), name='download_salary_slip'),
    path('user-salary-slip/', views.UserSalarySlipView.as_view(), name='user-salary-slip'),
    path('success-page/', views.success_page, name='success_page'),

]


    
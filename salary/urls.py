from django.urls import path
from . import views

urlpatterns = [

    path('generate-salary-slip/<int:id>/', views.GenerateSalarySlip.as_view(), name= "generate-salary-slip"),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee-list'),
    path('download-salary-slip/<int:id>/',views.DownloadSalarySlipView.as_view(), name='download_salary_slip'),
    path('user-salary-slip/', views.UserSalarySlipView.as_view(), name='user-salary-slip'),
    path('create-account/', views.CreateCustomer.as_view(), name = "create-customer"),
    path('creat-checkout-session/', views.CreateCheckoutSession.as_view(), name="creat-checkout-session")
   

]


    
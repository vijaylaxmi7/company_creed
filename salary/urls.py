from django.urls import path
from . import views

urlpatterns = [

    path('generate-salary-slip/<int:id>/', views.GenerateSalarySlip.as_view(), name= "generate-salary-slip"),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee-list')

]


    
from django.urls import path
from . import views

urlpatterns = [

    path('calculate-salary/<int:id>/', views.CalculateSalary.as_view(), name= "calculate-salary"),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee-list')

]


    
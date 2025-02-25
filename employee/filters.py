import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') # iexact searches without considering case sensitivity
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains') # icontains searches the word in substring without considering case sensitivity
    id = django_filters.RangeFilter(field_name='id') #is primary key it will not take emp_id 
    #if you pass emp_id it will give error as empid is charfield and pk is always interger field
    class Meta:
        model = Employee
        fields=['designation', 'emp_name', 'id']

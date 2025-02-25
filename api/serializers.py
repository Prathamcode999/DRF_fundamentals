from rest_framework import serializers
from students.models import Student
from employee.models import Employee

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


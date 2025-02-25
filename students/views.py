from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [
        {'id':1, 'name':'pratham', 'age':21}
    ]
    return HttpResponse(students)

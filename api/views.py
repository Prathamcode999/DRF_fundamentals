from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,Http404
from students.models import Student
from employee.models import Employee
from blogs.models import Blog,Comment
from blogs.serializers import blogSerializer, commentSerializer
from .serializers import studentSerializer, employeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from .paginations import CustomPagination
from employee.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter


#
# Function based views
#

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        #get all the data from student table
        students = Student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def studentsDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk) #getting student
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = studentSerializer(student) #converting the student model from dict to list using serializers
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = studentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#
#class based view
#

'''
class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = employeeSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = employeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class EmployeesDetail(APIView):
    def get_object(self, pk): 
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self,request ,pk):
        get_employee = self.get_object(pk)
        serializer = employeeSerializer(get_employee)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request,pk):
        get_employee = self.get_object(pk)
        serializer = employeeSerializer(get_employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request, pk):
        get_employee = self.get_object(pk)
        get_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


#
# mixin based views
#


'''
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): #listModelMixin gets the list of all the data from the databse, CreateModelMixin creates a data in database
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

    def get(self,request,pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
'''

#
# generic based views
#

'''
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'pk'
    '''

#
# view-sets(viewsets.Viewset)
# (needs router instead of url)
#

'''
class Employees(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = employeeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create (self, request):
        serialzier = employeeSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = employeeSerializer(employee)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = employeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

#
#viesets (viewset.ModelViewSet)
# it also need router
#

class Employees(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    pagination_class = CustomPagination # directly can be used with viewsets only
    filterset_class = EmployeeFilter

    # done with all pk and non pk operatiaons

#    
# blogs generics based views
#

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','^body'] #  add (^), this will stricly need the title's first word to search the blog
    ordering_fields = ['id']
    

class CommentView(generics.ListCreateAPIView):
    queryset= Comment.objects.all()
    serializer_class = commentSerializer

class BlogsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field = 'pk'

class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    lookup_field = 'pk'







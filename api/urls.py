from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.Employees, basename='employee') #dont need to mention if it's a class view (.as_view())


urlpatterns = [

    #students for function base view
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),

    #employee for class, mixins, generic based view
    # path('employees/', views.Employees.as_view()) ,
    # path('employees/<int:pk>/', views.EmployeesDetail.as_view()),

    #employee for viewset based views
    path('', include(router.urls)), #you dont need two urls, separate for pk

    #blog for generics based views
    path('blogs/', views.BlogsView.as_view()),
    path('comments/',views.CommentView.as_view()), #the above two are without pk
    path('blogs/<int:pk>',views.BlogsDetailView.as_view()),
    path('blogs/<int:pk>',views.CommentsDetailView.as_view()),


]

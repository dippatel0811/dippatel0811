from django.contrib import admin
from django.urls import include, path
from employee import views

urlpatterns = [
    path('addemployee/', views.addemployee),
    path('viewemployee/', views.viewemployee),
    path('employeepage/', views.employeepage),

]

from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.home, name="home"), 
    
    path('create/', views.create_student, name="create_student"),
    path('edit/<int:id>/', views.update_student, name="update_student"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),


]

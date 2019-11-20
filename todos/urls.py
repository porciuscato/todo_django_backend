from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('user/<int:pk>/', views.user_detail),
]
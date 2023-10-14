from django.urls import path

from project import views

urlpatterns = [
    path('', views.project_index),
    path('<int:pk>/', views.project_detail)
]

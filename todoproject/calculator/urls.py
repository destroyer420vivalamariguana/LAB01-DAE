from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:num1>/<int:num2>/', views.add, name='add'),
    path('subtract/<int:num1>/<int:num2>/', views.subtract, name='subtract'),
    path('multiply/<int:num1>/<int:num2>/', views.multiply, name='multiply'),
]

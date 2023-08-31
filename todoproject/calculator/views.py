from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add(request, num1, num2):
    result = int(num1) + int(num2)
    return HttpResponse(f"Sum: {num1} + {num2} = {result}")

def subtract(request, num1, num2):
    result = int(num1) - int(num2)
    return HttpResponse(f"Difference: {num1} - {num2} = {result}")

def multiply(request, num1, num2):
    result = int(num1) * int(num2)
    return HttpResponse(f"Product: {num1} * {num2} = {result}")


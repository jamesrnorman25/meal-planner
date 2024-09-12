from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

def new_mealplan(request):
    return HttpResponse()

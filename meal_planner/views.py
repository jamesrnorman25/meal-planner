from django.shortcuts import render
from django.http import HttpResponse

def create_account(request):
    return render(request, "create_account.html")

def homepage(request):
    return render(request, "home.html")
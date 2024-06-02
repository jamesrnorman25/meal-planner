from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Test homepage"""
    print(request)
    return HttpResponse("Yay, it worked!")

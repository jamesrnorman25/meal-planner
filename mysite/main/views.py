from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Test homepage"""
    return render(request=request, template_name="home.html", context=None)

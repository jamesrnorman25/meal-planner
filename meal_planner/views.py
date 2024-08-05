from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def create_account(request):
    if request.method == "POST":
        pass
    else:
        form = UserCreationForm
        return render(request, "create_account.html", context={"form": form})

def homepage(request):
    return render(request, "home.html")
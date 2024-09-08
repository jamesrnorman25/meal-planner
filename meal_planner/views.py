from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/Dashboard")
    else:
        form = UserCreationForm
        return render(request, "create_account.html", context={"form": form})

def homepage(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")
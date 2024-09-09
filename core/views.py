from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

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
    return render(request, "dashboard.html", context={"username": request.user.username})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            print("Form valid!")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User logged in successfully")
                login(request, user)
                return redirect("/Dashboard")
    else:
        form = AuthenticationForm
        return render(request, "login.html", context={"form": form})
from django import get_version
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mealplan.models import Mealplan

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/Dashboard")
        else:
            for message in form.error_messages:
                print(form.error_messages[message])
    else:
        form = UserCreationForm
    return render(request, "create_account.html", context={"form": form})

def homepage(request):
    print(get_version())
    return render(request, "home.html")

def dashboard(request):
    if request.user.is_authenticated:
        mealplans = Mealplan.objects.filter(user=request.user)
        # print(Mealplan.objects.all())
        # print([mealplan for mealplan in mealplans])
        # mealplan_ids = {mealplan.name: "_".join(mealplan.name.split(" ")) for mealplan in mealplans}
        return render(request, "dashboard.html", context={"mealplans": mealplans})
    else:
        return redirect("/Login")

def login_view(request):
    print(User.objects.all())
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        print(User.objects.all())
        if form.is_valid():
            # print("Form valid!")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # print("User logged in successfully")
                login(request, user)
                return redirect("/Dashboard")
        for message in form.error_messages:
            print(form.error_messages[message])
    else:
        form = AuthenticationForm
    return render(request, "login.html", context={"form": form})
    
def logout_view(request):
    logout(request)
    return redirect("/")
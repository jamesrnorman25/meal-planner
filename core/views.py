from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mealplan.models import Mealplan
from recipe.models import Recipe

import logging

logger = logging.getLogger(__name__)

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
    logger.info("Retrieving homepage")
    return render(request, "home.html")

def dashboard(request):
    if request.user.is_authenticated:
        mealplans = Mealplan.objects.filter(user=request.user)
        recipes = Recipe.objects.filter(user=request.user)
        logger.debug(Mealplan.objects.all())
        logger.debug([mealplan for mealplan in mealplans])
        # mealplan_ids = {mealplan.name: "_".join(mealplan.name.split(" ")) for mealplan in mealplans}
        return render(request, "dashboard.html", context={"mealplans": mealplans, "recipes": recipes})
    else:
        return redirect("/Login")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            logger.info("Form valid!")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # print("User logged in successfully")
                login(request, user)
                return redirect("/Dashboard")
    else:
        form = AuthenticationForm
    return render(request, "login.html", context={"form": form})
    
def logout_view(request):
    logout(request)
    return redirect("/")
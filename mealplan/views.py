from django.shortcuts import render, redirect
from django.http import HttpResponse
from mealplan.forms import MealplanForm

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

def new_mealplan(request):
    form = MealplanForm
    return render(request, "new.html", context={"form": form})

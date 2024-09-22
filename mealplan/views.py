from django.shortcuts import render, redirect
from django.http import HttpResponse
from mealplan.forms import MealplanForm

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

def existing_mealplan(request, slug):
    return HttpResponse()

def new_mealplan(request):
    if request.method == "POST":
        form = MealplanForm(request.POST)
        if form.is_valid():
            mealplan = form.save()
            return redirect("existing_mealplan", slug=mealplan.slug)
    else:
        form = MealplanForm
        return render(request, "new.html", context={"form": form})

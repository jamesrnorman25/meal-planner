from django.shortcuts import render, redirect
from django.http import HttpResponse
from mealplan.forms import MealplanForm
from mealplan.models import Mealplan

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

def existing_mealplan(request, slug):
    mealplan = Mealplan.objects.get(slug=slug)
    return render(request, "existing.html", context={"mealplan": mealplan})

def new_mealplan(request):
    if request.method == "POST":
        form = MealplanForm(request.POST)
        if form.is_valid():
            mealplan = form.save()
            return redirect("existing_mealplan", slug=mealplan.slug)
    else:
        form = MealplanForm
        return render(request, "new.html", context={"form": form})

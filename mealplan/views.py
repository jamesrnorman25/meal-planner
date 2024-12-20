from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mealplan.forms import MealplanForm
from mealplan.models import Mealplan

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

def existing_mealplan(request, slug):
    mealplan = Mealplan.objects.get(slug=slug)
    return render(request, "existing.html", context={"mealplan": mealplan})

def new_mealplan(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method == "POST":
            form = MealplanForm(request.POST)
            # print(form["user"])
            if form.is_valid():
                # form["user"] = user
                mealplan = form.save()
                mealplan.user = user
                mealplan.save()
                return redirect("existing_mealplan", slug=mealplan.slug)
            else:
                print("Form invalid")
        else:
            form = MealplanForm
        return render(request, "new.html", context={"form": form})
    else:
        return redirect("/Login")
    
def edit_mealplan(request, slug):
    mealplan = Mealplan.objects.get(slug=slug)
    if request.method == "POST":
        form = MealplanForm(data=request.POST, instance=mealplan)
        if form.is_valid():
            print(form["monday"])
            form.save()
            print(mealplan.monday)
            return redirect(f"/mealplans/{slug}")
    else:
        form = MealplanForm(instance=mealplan)
        return render(request, "edit.html", context={"form": form})

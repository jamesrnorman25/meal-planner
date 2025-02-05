from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from mealplan.models import Mealplan
from recipe.models import Recipe

import logging

logger = logging.getLogger(__name__)

class CreateAccountView(FormView):
    template_name = "create_account.html"
    form_class = UserCreationForm
    success_url = "/Dashboard"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# def create_account(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("/Dashboard")
#     else:
#         form = UserCreationForm
#     return render(request, "create_account.html", context={"form": form})

def homepage(request):
    logger.info("Retrieving homepage")
    return render(request, "home.html")

@login_required
def dashboard(request):
    mealplans = Mealplan.objects.filter(user=request.user)
    recipes = Recipe.objects.filter(user=request.user)
    logger.debug(Mealplan.objects.all())
    logger.debug([mealplan for mealplan in mealplans])
    # mealplan_ids = {mealplan.name: "_".join(mealplan.name.split(" ")) for mealplan in mealplans}
    return render(request, "dashboard.html", context={"mealplans": mealplans, "recipes": recipes})
import logging

from django.forms import inlineformset_factory
from django.shortcuts import render, HttpResponse, redirect
from recipe.forms import RecipeForm, RecipeIngredientForm
from recipe.models import Recipe, RecipeIngredient

logger = logging.getLogger(__name__)

# Create your views here.

def new_recipe(request):
    RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, fields=("ingredient", "quantity"))
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        logger.info(request.POST)
        form = RecipeForm(data=request.POST)
    recipe = Recipe()
    recipe.save()
    form = RecipeForm(instance=recipe)
    formset = RecipeIngredientFormSet(instance=recipe)
    

    return render(request, "new_recipe.html", context={"form": form, "formset": formset})

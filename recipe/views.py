import logging

from django.forms import formset_factory
from django.shortcuts import render, HttpResponse, redirect
from recipe.forms import RecipeForm, RecipeIngredientForm
from recipe.models import Recipe, RecipeIngredient
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

# Create your views here.

def new_recipe(request):
    RecipeIngredientFormSet = formset_factory(RecipeIngredientForm, extra=5, can_delete=True)
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        logger.info(request.POST)
        # Check recipe and save.
        form = RecipeForm(data=request.POST)
        formset = RecipeIngredientFormSet(data=request.POST)
        if form.is_valid():
            logger.info("Form is valid.")
            recipe = form.save(commit=False)
            recipe.user = User.objects.get(username=request.user.username)
            recipe.save()
            form.save_m2m()

            ingredients = formset.save(commit=False)
            for recipe_ingredient in ingredients:
                recipe_ingredient.recipe = recipe
                recipe_ingredient.save()
            formset.save_m2m()
            return redirect("/Dashboard")
        else:
            logger.info(f"Form bound: {form.is_bound}, Form valid: {form.is_valid()}")
            logger.info(f"Formset bound: {formset.is_bound}, Formset valid: {formset.is_valid()}")
            for error in form.errors:
                logger.error(error)
            for error in formset.errors:
                logger.error(error)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
    

    return render(request, "new_recipe.html", context={"form": form, "formset": formset})

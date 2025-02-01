import logging

from django.forms import modelformset_factory, formset_factory
from django.shortcuts import render, HttpResponse, redirect
from recipe.forms import RecipeForm, RecipeIngredientForm
from recipe.models import Recipe, RecipeIngredient
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)

def existing_recipe(request, slug):
    if not request.user.is_authenticated:
        return redirect("/Login")
    else:
        recipe = Recipe.objects.get(slug=slug)
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        return render(request, template_name="existing_recipe.html", context={"recipe": recipe, "ingredients": ingredients})


def edit_recipe(request, slug):
    if not request.user.is_authenticated:
        return redirect("/Login")
    else:
        # RecipeIngredientFormSet = formset_factory(RecipeIngredientForm, min_num=1, extra=0, can_delete=True)
        RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=0, can_delete=True)
        recipe = Recipe.objects.get(slug=slug)
        if request.method == "POST":
            form = RecipeForm(data=request.POST, instance=recipe)
            formset = RecipeIngredientFormSet(data=request.POST, queryset=RecipeIngredient.objects.filter(recipe=recipe))
            if form.is_valid() and formset.is_valid():
                recipe = form.save()
                for form in formset:
                    ingredient = form.cleaned_data.get("ingredient")
                    existing_recipe_ingredient = RecipeIngredient.objects.get(ingredient=ingredient, recipe=recipe)
                    if existing_recipe:
                        new_form = RecipeIngredientForm(data=form.cleaned_data, instance=existing_recipe_ingredient)
                        new_form.save()
                # formset.save_m2m()
                return redirect("existing_recipe", slug=recipe.slug)
        else:
            form = RecipeForm(instance=recipe)
            # ingredients = [RecipeIngredientForm(instance=recipe_ingredient) for recipe_ingredient in RecipeIngredient.objects.filter(recipe=recipe)]
            formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.filter(recipe=recipe))
                
        return render(request, template_name="edit_recipe.html", context={"form": form, "formset": formset})

def new_recipe(request):
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm)
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        logger.info(f"Post request submitted to /recipes/new with data \n{request.POST}")
        # Check recipe and save.
        form = RecipeForm(data=request.POST)
        formset = RecipeIngredientFormSet(data=request.POST)
        if form.is_valid():
            logger.info("Form is valid.")
            recipe = form.save(commit=False)
            recipe.user = User.objects.get(username=request.user.username)
            recipe.save()
            form.save_m2m()
            if formset.is_valid():
                logger.info("Formset is valid.")
                logger.info(formset)
                for ingredient_form in formset:
                    recipe_ingredient = ingredient_form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
                    ingredient_form.save_m2m()
                return redirect("existing_recipe", slug=recipe.slug)
        else:
            logger.error(f"Form bound: {form.is_bound}, Form valid: {form.is_valid()}")
            logger.error(f"Formset bound: {formset.is_bound}, Formset valid: {formset.is_valid()}")
            for error in form.errors:
                logger.error(error)
            for error in formset.errors:
                logger.error(error)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
    

    return render(request, "new_recipe.html", context={"form": form, "formset": formset})

class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = "delete_recipe.html"
    success_url = reverse_lazy("dashboard")

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/Login")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/Login")
        return super().post(request, *args, **kwargs)

from django import forms
from recipe.models import Recipe, Ingredient
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("name", "ingredients", "method")

    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())

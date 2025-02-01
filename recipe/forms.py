from django import forms
from recipe.models import Recipe, Ingredient, RecipeIngredient
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("name", "method")



class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("ingredient", "quantity",)
        
    # ingredient = IngredientMCF(queryset=Ingredient.objects.all())



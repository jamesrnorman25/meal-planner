from django import forms
from recipe.models import Recipe, Ingredient, RecipeIngredient
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("name", "method")

class IngredientMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("ingredient", "quantity")
        widgets = {"ingredient": IngredientMCF(queryset=Ingredient.objects.all())}


# RecipeIngredientFormset = forms.formset_factory(RecipeIngredientForm, 1, )
from django.contrib import admin

from recipe.models import Ingredient, Recipe

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display=("name",)
    fields=["name",]

class RecipeAdmin(admin.ModelAdmin):
    list_display=("name",)
    fields=["name", "method"]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
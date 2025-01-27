from django.contrib import admin

from recipe.models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display=("name",)
    fields=["name",]

class RecipeAdmin(admin.ModelAdmin):
    list_display=("name",)
    fields=["name", "method"]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display=("recipe", "ingredient", "quantity")
    fields=["recipe", "ingredient", "quantity"]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

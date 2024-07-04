from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    """Admin for recipe model."""
    fields = ["recipe_name",
              "recipe_prep_time",
              "recipe_prep_time_unit"]
    through_fields = ["recipe_ingredients"]
    list_display = ["recipe_name"]

class IngredientAdmin(admin.ModelAdmin):
    """Admin for ingredient model."""
    fields = ["ingredient_name",
              "ingredient_min_buying_size",
              "ingredient_count_unit"]
    list_display = ["ingredient_name"]

class RecipeIngredientAdmin(admin.ModelAdmin):
    """Model admin for custom manytomany field"""
    fields = ["recipe", "ingredient", "ingredient_amount"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

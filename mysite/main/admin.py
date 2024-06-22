from django.contrib import admin
from .models import Recipe, Ingredient

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    """Admin for recipe model."""
    fields = ["recipe_name",
              "recipe_prep_time",
              "recipe_prep_time_unit",
              "recipe_ingredients"]
    list_display = [field.name for field in Recipe._meta.get_fields()][1:-2]

class IngredientAdmin(admin.ModelAdmin):
    """Admin for ingredient model."""
    fields = ["ingredient_name",
              "ingredient_min_buying_size",
              "ingredient_count_unit"]
    list_display = [field.name for field in Ingredient._meta.get_fields()][1:]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

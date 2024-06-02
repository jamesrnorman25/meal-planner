from django.contrib import admin
from .models import Recipe, Ingredient

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    fields = ["recipe_name",
              "recipe_prep_time",
              "recipe_prep_time_unit"]
    list_display = [field.name for field in Recipe._meta.get_fields()]
    

class IngredientAdmin(admin.ModelAdmin):
    fields = ["ingredient_name",
              "ingredient_min_buying_size",
              "ingredient_count_unit"]
    list_display = [field.name for field in Ingredient._meta.get_fields()]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

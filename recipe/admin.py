from django.contrib import admin

from recipe.models import Ingredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display=("name",)
    fields=["name",]

admin.site.register(Ingredient, IngredientAdmin)

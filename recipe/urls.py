from django.urls import path
import recipe.views as views

urlpatterns = [
    path("new", views.new_recipe, name="new_recipe"),
    path("<slug:slug>", views.existing_recipe, name="existing_recipe"),
]
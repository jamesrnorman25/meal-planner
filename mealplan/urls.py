from django.urls import path
import mealplan.views as views

urlpatterns = [
    path('', views.blank, name="empty_mealplan"),
    path('new', views.new_mealplan, name="new_mealplan"),
]
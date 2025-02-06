from django.urls import path
import mealplan.views as views

urlpatterns = [
    path('', views.blank, name="empty_mealplan"),
    path('new', views.MealplanCreateView.as_view(), name="new_mealplan"),
    path('<slug:slug>', views.MealplanDetailView.as_view(), name="mealplan_detail"),
    path('<slug:slug>/edit', views.MealplanUpdateView.as_view(), name="mealplan_update"),
]
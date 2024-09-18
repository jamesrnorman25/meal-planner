from django import forms
from mealplan.models import Mealplan

class MealplanForm(forms.models.ModelForm):
    class Meta:
        model = Mealplan
        fields = ("name", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",)
        widgets = {
            "name": forms.widgets.TextInput(attrs={"placeholder": "Name"}),
            "monday": forms.widgets.TextInput(attrs={"placeholder": "Monday"}),
            "tuesday": forms.widgets.TextInput(attrs={"placeholder": "Tuesday"}),
            "wednesday": forms.widgets.TextInput(attrs={"placeholder": "Wednesday"}),
            "thursday": forms.widgets.TextInput(attrs={"placeholder": "Thursday"}),
            "friday": forms.widgets.TextInput(attrs={"placeholder": "Friday"}),
            "saturday": forms.widgets.TextInput(attrs={"placeholder": "Saturday"}),
            "sunday": forms.widgets.TextInput(attrs={"placeholder": "Sunday"}),
        }
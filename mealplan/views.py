import logging

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from mealplan.forms import MealplanForm
from mealplan.models import Mealplan

logger = logging.getLogger(__name__)

# Create your views here.

def blank(request):
    return redirect("new_mealplan")

class MealplanDetailView(DetailView):
    model = Mealplan
    template_name = "existing.html"
    context_object_name = "mealplan"


class MealplanCreateView(LoginRequiredMixin, CreateView):
    model = Mealplan
    form_class = MealplanForm
    template_name = "new.html"

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user.username)
        mealplan = form.save()
        mealplan.user = user
        mealplan.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mealplans"] = Mealplan.objects.filter(user=self.request.user)
        return context
    
    def get_success_url(self):
        return reverse("mealplan_detail", kwargs={"slug": self.object.slug})


class MealplanUpdateView(LoginRequiredMixin, UpdateView):
    model = Mealplan
    form_class = MealplanForm
    template_name = "edit.html"

    def get_success_url(self):
        return reverse("mealplan_detail", kwargs={"slug": self.object.slug})
    

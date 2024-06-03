"""View configuration for meal planner"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .models import Recipe


# Create your views here.
def landing_page(request):
    """Redirects to homepage (allows landing page to be changed later)"""
    del request
    return redirect("main:homepage")

def homepage(request):
    """Test homepage"""
    return render(request=request, template_name="home.html", context=None)


def login_page(request):
    """User login code"""
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:homepage")


    else:
        form = AuthenticationForm
        return render(request=request, template_name="login.html", context={"form": form})


def logout_request(request):
    """Logs out the user"""
    logout(request)
    return redirect("main:home")


def recipe_browse_page(request):
    """Returns recipe browser page"""
    return render(request=request, template_name="all_recipes.html", context={"recipes": Recipe._meta.objects.all})


def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = UserCreationForm
        return render(request=request, template_name="register.html", context={"form": form})

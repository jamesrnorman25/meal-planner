from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("Home", views.homepage, name="homepage"),
    path("Sign_up", views.signup_page, name="signup_page"),
    path("Login", views.login_page, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("browse-recipes", views.recipe_browse_page, name="browse-recipes")
]

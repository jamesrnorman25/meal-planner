"""dev_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from mealplan import urls as mealplan_urls
from recipe import urls as recipe_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.homepage),
    path('Create-Account', core_views.create_account),
    path('Dashboard', core_views.dashboard),
    path('Login', core_views.login_view),
    path('Logout', core_views.logout_view),
    path('mealplans/', include(mealplan_urls)),
    path('recipes/', include(recipe_urls)),
]

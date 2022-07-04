"""mybecofeWINDOWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import (home_page, users_url, promo_url, recipe_url)
from becoffe_app.views import user_detail

urlpatterns = [
    path('leo-admin/', admin.site.urls),
    path('', home_page),
    path('api/users', users_url),
    path('api/promo', promo_url),
    path('api/recipe', recipe_url),
    path('api/details', user_detail),
]

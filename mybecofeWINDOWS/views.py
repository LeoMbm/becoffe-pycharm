from django.http import HttpResponse
from django.shortcuts import render


def home_views(request):
    my_title = "myBecoffe - Home"
    tabs_title = "myBecoffe - Home"
    return render(request, "home.html", {"title": my_title, "tabs": tabs_title})


def login_views(request):
    my_title = "myBecoffe - Login"
    tabs_title = "myBecoffe - Login"
    return render(request, "login.html", {"title": my_title, "tabs": tabs_title})


def register_views(request):
    my_title = "myBecoffe - Register"
    tabs_title = "myBecoffe - Register"
    return render(request, "register.html", {"title": my_title, "tabs": tabs_title})


def users_views(request):
    return render(request, "users.html",
                  {"title": "Api for users", "tabs": "myBecoffe - Users", "my_list": [1, 2, 3, 4, 5]})


def promo_views(request):
    return render(request, "promo.html", {"title": "Api for promo", "tabs": "myBecoffe - Promo"})


def recipe_views(request):
    return render(request, "recipe.html", {"title": "Api for becoffe_app", "tabs": "myBecoffe - Recipe"})

# DONE : HERE WE HAVE GENERATED THE TITLE DYNAMICALLY

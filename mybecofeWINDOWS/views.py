from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "myBecoffe - Home"
    tabs_title = "myBecoffe - Home"
    return render(request, "home.html", {"title": my_title, "tabs": tabs_title})


def users_url(request):
    return render(request, "users.html",
                  {"title": "Render from users", "tabs": "myBecoffe - Users", "my_list": [1, 2, 3, 4, 5]})


def promo_url(request):
    return render(request, "promo.html", {"title": "Render from promo", "tabs": "myBecoffe - Promo"})


def recipe_url(request):
    return render(request, "recipe.html", {"title": "Render from becoffe_app", "tabs": "myBecoffe - Recipe"})

# DONE : HERE WE HAVE GENERATED THE TITLE DYNAMICALLY

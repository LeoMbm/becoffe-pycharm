from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


def login_views(request):
    my_title = "myBecoffe - Login"
    tabs_title = "myBecoffe - Login"
    return render(request, "registration/login.html", {"title": my_title, "tabs": tabs_title})


def register_views(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect("/login")
    else:
        form = RegisterForm()

    my_title = "myBecoffe - Register"
    tabs_title = "myBecoffe - Register"
    return render(request, "registration/sign-up.html", {"title": my_title, "tabs": tabs_title, "form": form})


@login_required(login_url="/login")
def home_views(request):
    my_title = "myBecoffe - Home"
    tabs_title = "myBecoffe - Home"
    return render(request, "home.html", {"title": my_title, "tabs": tabs_title})


@login_required(login_url="/login")
def users_views(request):
    return render(request, "users.html",
                  {"title": "Api for users", "tabs": "myBecoffe - Users", "my_list": [1, 2, 3, 4, 5]})


@login_required(login_url="/login")
def promo_views(request):
    return render(request, "promo.html", {"title": "Api for promo", "tabs": "myBecoffe - Promo"})


@login_required(login_url="/login")
def recipe_views(request):
    return render(request, "recipe.html", {"title": "Api for main", "tabs": "myBecoffe - Recipe"})

# DONE : HERE WE HAVE GENERATED THE TITLE DYNAMICALLY

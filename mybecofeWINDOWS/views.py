from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "index.html")


def users_url(request):
    return HttpResponse("<h1>Hello Users</1>")


def promo_url(request):
    return HttpResponse("<h1>Hello Promo</1>")


def recipe_url(request):
    return HttpResponse("<h1>Hello Recipe</1>")

from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Users, Recipe, Promo

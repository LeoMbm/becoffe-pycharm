from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Users, Recipe, Promo


def user_detail_view(request, user_id):
    # try:
    #     obj = Users.objects.get(id=str(user_id))
    # except Users.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    obj = get_object_or_404(Users, id=str(user_id))
    template_name = 'user_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def recipe_list_view(request):
    # list out objects, could be search
    qs = Recipe.objects.all()
    template_name = 'recipe_list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def recipe_create_view(request):
    # Create Objects ? with a form
    template_name = 'recipe_create.html'
    context = {"form": None}
    return render(request, template_name, context)


def recipe_detail_view(request, recipe_id):
    # 1 Object -> detail view
    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def recipe_update_view(request, recipe_id):
    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def recipe_delete_view(request, recipe_id):
    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)

# TODO: SECTION 7

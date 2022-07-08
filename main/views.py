from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from mybecofeWINDOWS.forms import RecipeForm
from .models import user, Recipe, Promo


@login_required(login_url='/login')
def user_detail_view(request, user_id):
    # try:
    #     obj = Users.objects.get(id=str(user_id))
    # except Users.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    obj = get_object_or_404(user, id=str(user_id))
    template_name = 'user_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_list_view(request):
    # list out objects, could be search
    qs = Recipe.objects.all()
    template_name = 'recipe_list.html'
    context = {"recipe_list": qs}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_create_view(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author_id_id = request.user.id
        recipe.save()
        return redirect('/')
    else:
        form = RecipeForm()
    print(request.user.id)
    return render(request, 'recipe_create.html', {"form": form})


@login_required(login_url='/login')
def recipe_detail_view(request, recipe_id):
    # 1 Object -> detail view
    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_detail.html'
    context = {"recipe": obj}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_update_view(request, recipe_id):
    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_update.html'
    context = {"recipe": obj, 'form': None}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_delete_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        r_id = request.POST.get('recipe-id')
        recipe.delete()
        return redirect('/')

    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_delete.html'
    context = {"recipe": obj}
    return render(request, template_name, context)

# TODO: SECTION 7

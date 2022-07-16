from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from mybecofeWINDOWS.forms import RecipeForm, RegisterForm, EditProfileForm, EditRecipeForm, CreatePromoForm, \
    EditPromoForm
from .models import user, Recipe, Promo, userInPromo


@login_required(login_url='/login')
def user_detail_view(request, user_id):
    if request.method == "POST":
        u_id = request.POST.get('user-id')
        userToDelete = user.objects.filter(id=u_id)
        userToDelete.delete()
        return redirect('/users')
    obj = get_object_or_404(user, id=str(user_id))
    template_name = 'user_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@login_required(login_url='/login')
def user_edit_view(request, user_id):
    # FIXME: Can't upload profile picture in edit view
    obj = get_object_or_404(user.objects.filter(id=str(user_id)))
    msg = None
    form = EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        msg = 'Data Successfully changed'
        return redirect('/users')

    form = EditProfileForm(instance=obj)
    template_name = 'edit_profile.html'
    context = {"form": form, "profile": obj, "msg": msg}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_list_view(request):
    # list out objects, could be search
    if request.method == "POST":
        r_id = request.POST.get('recipe-id')
        recipeToDelete = Recipe.objects.filter(id=r_id)
        recipeToDelete.delete()
        return redirect('/recipe')
    qs = Recipe.objects.all().select_related('author_id')
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
    obj = get_object_or_404(Recipe.objects.filter(id=str(recipe_id)).select_related("author_id"), id=str(recipe_id))
    template_name = 'recipe_detail.html'
    context = {"recipe": obj}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_update_view(request, recipe_id):
    obj = get_object_or_404(Recipe.objects.filter(id=str(recipe_id)).select_related("author_id"), id=str(recipe_id))
    obj2 = get_object_or_404(Recipe.objects.filter(id=str(recipe_id)))
    form = EditRecipeForm()
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/recipe')
    else:
        form = RecipeForm(instance=obj)
    template_name = 'recipe_update.html'
    context = {"recipe": obj, 'form': form, "profile": obj2}
    return render(request, template_name, context)


@login_required(login_url='/login')
def recipe_delete_view(request, recipe_id):
    recipe = get_object_or_404(Recipe.objects.filter(id=str(recipe_id)).select_related("author_id"), id=str(recipe_id))
    if request.method == "POST":
        r_id = request.POST.get('recipe-id')
        recipe.delete()
        return redirect('/')

    obj = get_object_or_404(Recipe, id=str(recipe_id))
    template_name = 'recipe_delete.html'
    context = {"recipe": obj}
    return render(request, template_name, context)


@login_required(login_url='/login')
def promo_create_view(request):
    form = CreatePromoForm()
    if request.method == 'POST':
        form = CreatePromoForm(request.POST)
    if form.is_valid():
        promo = form.save(commit=False)
        promo.admin_id_id = request.user.id
        promo.save()
        return redirect('/')
    else:
        form = CreatePromoForm()
    print(request.user.id)
    return render(request, 'promo_create.html', {"form": form})


@login_required(login_url='/login')
def promo_list_view(request):
    if request.method == "POST":
        p_id = request.POST.get('promo-id')
        promoToDelete = Promo.objects.filter(id=p_id)
        promoToDelete.delete()
        return redirect('/promo')
    qs = Promo.objects.all()
    template_name = 'promo.html'
    context = {"promo": qs}
    return render(request, template_name, context)


@login_required(login_url='/login')
def promo_detail_view(request, promo_id):
    obj = userInPromo.objects.filter(promo_id_id=str(promo_id)).select_related("user_id")
    template_name = 'promo_detail.html'
    context = {"u_promo": obj}
    return render(request, template_name, context)


def promo_edit_view(request, promo_id):
    obj = get_object_or_404(Promo.objects.filter(id=str(promo_id)).select_related("admin_id"), id=str(promo_id))
    form = EditPromoForm()
    if request.method == 'POST':
        form = EditPromoForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/promo')
    else:
        form = EditPromoForm(instance=obj)
    template_name = 'recipe_update.html'
    context = {"promo": obj, 'form': form}
    return render(request, template_name, context)


def promo_add_user_view(request, promo_id):
    obj = user.objects.all()
    if request.method == 'POST':
        p_id = request.POST.getlist('user-to-add')
        target = userInPromo(promo_id_id=promo_id, user_id_id=p_id)
        target.save()
        return redirect('/promo')

    template_name = 'promo_adduser.html'
    context = {"users": obj}
    return render(request, template_name, context)

# ADD USER IN PROMO

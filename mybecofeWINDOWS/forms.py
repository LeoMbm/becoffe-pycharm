from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from main.models import Recipe, Promo

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "is_superuser", "profil_pic"]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "profil_pic", "is_superuser"]


class RecipeForm(forms.ModelForm):
    preview_at = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Recipe
        fields = ["title", "preview_at"]


class EditRecipeForm(forms.ModelForm):
    preview_at = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Recipe
        fields = ["title", "preview_at"]


class CreatePromoForm(forms.ModelForm):
    class Meta:
        model = Promo
        fields = ["name"]

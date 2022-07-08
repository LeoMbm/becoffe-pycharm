from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from main.models import Recipe

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "Chef"]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "preview_at"]

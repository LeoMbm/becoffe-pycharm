from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField()

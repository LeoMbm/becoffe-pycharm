from django.urls import path
from .views import (user_detail_view, recipe_list_view, recipe_create_view, recipe_update_view,
                    recipe_delete_view, recipe_detail_view)

urlpatterns = [

    path('', recipe_list_view),
    path('<int:recipe_id>/', recipe_detail_view),
    path('<int:recipe_id>/edit/', recipe_update_view),
    path('<int:recipe_id>/delete/', recipe_delete_view),
]

# FIXME: NEED TO TRANSLATE THAT FOR REGISTRATION

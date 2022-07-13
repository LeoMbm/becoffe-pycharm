"""mybecofeWINDOWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (home_views, users_views, promo_views, recipe_views, register_views)
from main.views import (user_detail_view, recipe_create_view, user_edit_view, promo_create_view, promo_list_view,
                        promo_detail_view, promo_edit_view, promo_add_user_view)

urlpatterns = [
    path('recipe/', include('main.urls')),
    path('recipe/create/', recipe_create_view),
    path('', include('django.contrib.auth.urls')),
    path('', home_views),
    path('sign-up/', register_views, name='sign-up'),
    path('users/', users_views),
    path('users/<int:user_id>/', user_detail_view),
    path('users/<int:user_id>/edit', user_edit_view),
    path('promo/', promo_list_view),
    path('promo/create/', promo_create_view),
    path('promo/<int:promo_id>/', promo_detail_view),
    path('promo/<int:promo_id>/edit', promo_edit_view),
    path('promo/<int:promo_id>/add', promo_add_user_view),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TODO: Functionnality for promo

from django.contrib import admin

# Register your models here.
from .models import (user, Promo, userInPromo, Recipe, Attendees)

admin.site.register(user)
admin.site.register(Promo)
admin.site.register(Recipe)
admin.site.register(userInPromo)
admin.site.register(Attendees)

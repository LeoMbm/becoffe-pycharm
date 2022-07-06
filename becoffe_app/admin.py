from django.contrib import admin

# Register your models here.
from .models import (Users, Promo, UsersInPromo, Recipe, Attendees)

admin.site.register(Users)
admin.site.register(Promo)
admin.site.register(Recipe)
admin.site.register(UsersInPromo)
admin.site.register(Attendees)

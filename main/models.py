import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class user(AbstractUser):
    Chef = models.BooleanField(default=False)


class Promo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    admin_id = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=django.utils.timezone.now)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    author_id = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    preview_at = models.DateTimeField(default=django.utils.timezone.now, unique_for_date=True)


class Attendees(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(default=django.utils.timezone.now)
    departure_time = models.DateTimeField(default=django.utils.timezone.now)


class userInPromo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    promo_id = models.ForeignKey(Promo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)

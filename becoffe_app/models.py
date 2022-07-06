import django.utils.timezone
from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    Admin = models.BooleanField()
    created_at = models.DateTimeField(default=django.utils.timezone.now)


class Promo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    admin_id = models.IntegerField()
    created_at = models.DateTimeField(default=django.utils.timezone.now)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    author_id = models.IntegerField()
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    preview_at = models.DateTimeField(default=django.utils.timezone.now, unique_for_date=True)


class Attendees(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.IntegerField()
    arrival_time = models.DateTimeField(default=django.utils.timezone.now)
    departure_time = models.DateTimeField(default=django.utils.timezone.now)


class UsersInPromo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    promo_id = models.IntegerField()
    user_id = models.IntegerField()

# FIXME: FIX PROBLEM WITH MIGRATIONS AND DATE AT LINE 27

from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    Admin = models.BooleanField()
    created_at = models.DateField()


class Promo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    admin_id = models.CharField(max_length=100)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    author_id = models.CharField(max_length=100)


class Attendees(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.CharField(max_length=100)
    arrival_time = models.DateField(max_length=100)
    departure_time = models.DateField(max_length=100)


0

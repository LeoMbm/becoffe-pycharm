from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    account_type = models.BooleanField()
    created_at = models.DateTimeField()


class Promo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    admin_id = models.ForeignKey(Users.id, max_length=100)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    author_id = models.ForeignKey(Users.id, on_delete=True)


class Attendees(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users.id, on_delete=True)
    arrival_time = models.DateTimeField(max_length=100)
    departure_time = models.DateTimeField(max_length=100)

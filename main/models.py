from django.contrib.auth.models import AbstractUser
from django.db import models


class user(AbstractUser):
    Chef = models.BooleanField(default=False)
    profil_pic = models.ImageField(null=True, blank=True, upload_to="images/")


class Promo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    admin_id = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    author_id = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    preview_at = models.DateField(auto_now_add=False, unique_for_date='preview_at')


class Attendees(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(auto_now_add=True)


class userInPromo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    promo_id = models.ForeignKey(Promo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)

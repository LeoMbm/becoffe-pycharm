# Generated by Django 4.0.5 on 2022-07-06 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('becoffe_app', '0002_attendees_usersinpromo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preview_at',
            field=models.DateTimeField(default=django.utils.timezone.now, unique_for_date=True),
        ),
    ]
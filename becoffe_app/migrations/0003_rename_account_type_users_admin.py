# Generated by Django 4.0.5 on 2022-07-04 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('becoffe_app', '0002_attendees_users_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='account_type',
            new_name='Admin',
        ),
    ]
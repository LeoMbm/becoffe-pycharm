# Generated by Django 4.0.5 on 2022-07-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_profil_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profil_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

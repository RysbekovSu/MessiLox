# Generated by Django 5.0.6 on 2024-05-23 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_food_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
    ]
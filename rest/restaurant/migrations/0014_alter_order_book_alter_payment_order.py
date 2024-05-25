# Generated by Django 5.0.6 on 2024-05-25 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.book'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order'),
        ),
    ]

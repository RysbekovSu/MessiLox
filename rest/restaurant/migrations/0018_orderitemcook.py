# Generated by Django 5.0.6 on 2024-05-28 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_book_unique_time_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemCook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderItem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.orderitem')),
            ],
        ),
    ]
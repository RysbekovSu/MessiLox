# Generated by Django 5.0.6 on 2024-05-24 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_book_table_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.book', unique=True),
        ),
    ]

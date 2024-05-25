# Generated by Django 5.0.6 on 2024-05-25 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_alter_order_book_alter_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='food',
            field=models.ForeignKey(db_column='food_name', null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.food', to_field='name'),
        ),
    ]

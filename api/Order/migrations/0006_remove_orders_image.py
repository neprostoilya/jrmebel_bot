# Generated by Django 5.0 on 2023-12-30 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_remove_orders_color_remove_orders_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='image',
        ),
    ]

# Generated by Django 5.0 on 2024-01-30 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_alter_furnitures_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='styles',
            name='category',
            field=models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, to='Catalog.categories', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]

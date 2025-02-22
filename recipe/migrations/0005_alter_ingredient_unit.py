# Generated by Django 5.1 on 2025-02-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('ml', 'ml'), ('l', 'l'), ('tbsp', 'tbsp'), ('tsp', 'tsp'), ('cup', 'cup'), ('none', 'No unit'), ('slices', 'slices')], default='none', max_length=100),
        ),
    ]

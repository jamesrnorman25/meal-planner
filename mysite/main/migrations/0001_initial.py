# Generated by Django 5.0.6 on 2024-06-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=100)),
                ('ingredient_count_unit', models.CharField(choices=[('count', ''), ('g', 'g'), ('ml', 'ml'), ('tsp', 'tsp'), ('tbsp', 'tbsp')], max_length=10)),
                ('ingredient_min_buying_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=300)),
                ('recipe_prep_time', models.IntegerField()),
                ('recipe_prep_time_unit', models.CharField(choices=[('min', 'minutes'), ('hr', 'hours')], max_length=20)),
            ],
        ),
    ]

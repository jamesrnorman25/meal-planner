# Generated by Django 5.1 on 2024-09-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='friday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='monday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='saturday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='sunday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='thursday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='tuesday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='wednesday',
            field=models.CharField(default='', max_length=100),
        ),
    ]

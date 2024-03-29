# Generated by Django 4.2.7 on 2024-01-14 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_meal_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='calories_total',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='carbs_total',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='description_diet',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='fats_total',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='protein_total',
        ),
        migrations.AddField(
            model_name='dishes',
            name='calories_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dishes',
            name='carbs_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dishes',
            name='fats_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dishes',
            name='protein_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-14 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_remove_diet_calories_total_remove_diet_carbs_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_number',
            field=models.PositiveIntegerField(choices=[('breakfast', 'Breakfast'), ('second_breakfast', 'Second breakfast'), ('lunch', 'Lunch'), ('afternoon_snack', 'Afternoon snack'), ('dinner', 'Dinner')]),
        ),
    ]

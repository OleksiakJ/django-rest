# Generated by Django 4.2.7 on 2024-01-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_alter_exercise_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]

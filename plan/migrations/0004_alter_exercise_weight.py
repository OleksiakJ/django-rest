# Generated by Django 4.2.7 on 2024-01-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_exercise_reps_alter_exercise_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.PositiveIntegerField(default=0, max_length=100),
        ),
    ]

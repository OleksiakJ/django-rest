# Generated by Django 4.2.7 on 2024-01-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0009_alter_exercise_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingplan',
            name='goal',
            field=models.CharField(default='', max_length=100),
        ),
    ]
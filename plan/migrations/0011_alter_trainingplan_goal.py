# Generated by Django 4.2.7 on 2024-01-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_trainingplan_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingplan',
            name='goal',
            field=models.CharField(default='Plan treningowy', max_length=100),
        ),
    ]
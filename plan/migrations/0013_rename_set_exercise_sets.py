# Generated by Django 4.2.7 on 2024-01-13 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0012_alter_trainingplan_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='set',
            new_name='sets',
        ),
    ]

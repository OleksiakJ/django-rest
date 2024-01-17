# Generated by Django 4.2.7 on 2024-01-16 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0006_remove_trainer_average_rating_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diet', '0013_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_diet', models.CharField(max_length=255)),
                ('description_diet', models.TextField(default='')),
                ('dishes', models.ManyToManyField(to='diet.dishes')),
                ('trainer_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diets_trainer', to='coach.trainer')),
                ('user_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diets_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
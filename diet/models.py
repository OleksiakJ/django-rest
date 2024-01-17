from django.db import models
from user.models import User
from coach.models import Trainer

class Meal(models.Model):
    name_meal = models.CharField(max_length=255)
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('second_breakfast', 'Second breakfast'),
        ('lunch', 'Lunch'),
        ('afternoon_snack', 'Afternoon snack'),
        ('dinner', 'Dinner'),
    ]
    meal_number = models.CharField(max_length=100, choices=MEAL_CHOICES)
    hour = models.TimeField()
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    recipe = models.TextField(default='Brak przepisu')

    def __str__(self):
        return f"{self.meal_number}: {self.name_meal}"

class Dishes(models.Model):
    days_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    days = models.CharField(max_length=100, choices=days_choices)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return f"{self.days}"


class Diet(models.Model):
    name_diet = models.CharField(max_length=255)
    dishes = models.ManyToManyField(Dishes)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='diets_user')
    trainer= models.ForeignKey(Trainer, on_delete=models.CASCADE,related_name='diets_trainer')
    description_diet = models.TextField(default='')


    def __str__(self):
        return f"{self.name_diet} dla {self.user} stworzona przez {self.trainer}"


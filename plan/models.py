from django.db import models
from user.models import User
from coach.models import Trainer


class Exercise(models.Model):
    name_exercise = models.CharField(max_length=255)
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight = models.CharField(max_length=100, null=True, blank=True, default=0)
    url_exercise = models.URLField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_exercise}"


class ExerciseSet(models.Model):
    name_set = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.name_set}"


class TrainingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_plans_user')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='training_plans_trainer')
    goal = models.CharField(max_length=100)
    exercise_set = models.ManyToManyField(ExerciseSet)

    def __str__(self):
        return f"{self.goal} dla {self.user} stworzony przez {self.trainer}"


class ProgressVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    exercise_set = models.ForeignKey(ExerciseSet, on_delete=models.CASCADE)
    completed_exercises = models.ManyToManyField('plan.Exercise', blank=True)
    verified = models.BooleanField(default=False)
    date_verified = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.exercise_set} - Verified: {self.verified}"

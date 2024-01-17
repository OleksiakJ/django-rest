from django.db import models
from user.models import User
from coach.models import Trainer


class WorkingDay(models.Model):
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} {self.start_time} - {self.end_time}"


class WorkPlan(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    working_days = models.ManyToManyField(WorkingDay)

    def __str__(self):
        return f"Kalendarz zajeć {self.trainer}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Rezerwacja {self.user} - {self.trainer} dnia {self.date} w godzinach {self.start_time} - {self.end_time} "




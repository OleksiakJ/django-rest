from django.db import models
from user.models import User


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)

    def calculate_average_rating(self):
        ratings = Rating.objects.filter(trainer=self)
        total_points = sum(rating.rating_value for rating in ratings)
        total_weights = len(ratings)

        if total_weights > 0:
            avg = total_points / total_weights
            return round(avg, 2)
        else:
            return None


    def calculate_number_of_votes(self):
        ratings = Rating.objects.filter(trainer=self)
        return len(ratings)



    def __str__(self):
        return f"{self.name} {self.surname}"



class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating_value = models.PositiveIntegerField(choices=RATING_CHOICES)
    comments = models.TextField(null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='trainer_ratings')
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_added', 'trainer')

    def __str__(self):
        return f'Rating for {self.trainer} by {self.user_added}'

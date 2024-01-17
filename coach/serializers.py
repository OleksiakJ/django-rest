from rest_framework import serializers
from .models import Trainer, Rating
from user.serializers import UserSerializer


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Trainer
        fields = ['id', 'name', 'surname', 'mail', 'average_rating', 'total_votes']

    def get_average_rating(self, trainer):
        return trainer.calculate_average_rating()

    def get_total_votes(self, trainer):
        return trainer.calculate_number_of_votes()


class RatingSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    trainer = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all())

    class Meta:
        model = Rating
        fields = ('user_added', 'trainer', 'rating_value', 'comments', 'date_added')
        read_only_fields = ('date_added', 'user_added')


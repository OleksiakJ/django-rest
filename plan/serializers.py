from rest_framework import serializers
from plan import models
from coach.serializers import TrainerSerializer
from user.serializers import UserSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ('name_exercise', 'url_exercise', 'description', 'sets', 'reps', 'weight')

class ExerciseSetSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = models.ExerciseSet
        fields = ('name_set', 'exercises')


class TrainingPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)
    exercise_set = ExerciseSetSerializer(read_only=True, many=True)

    class Meta:
        model = models.TrainingPlan
        fields = ('user', 'trainer', 'goal', 'exercise_set')


class ProgressVerificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)
    training_plan = TrainingPlanSerializer()

    class Meta:
        model = models.ProgressVerification
        fields = ('user', 'trainer', 'training_plan')





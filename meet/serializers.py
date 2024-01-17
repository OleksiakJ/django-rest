from rest_framework import serializers
from .models import Reservation, WorkPlan, WorkingDay
from coach.models import Trainer
from user.serializers import UserSerializer


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ['id', 'day', 'start_time', 'end_time']


class WorkPlanSerializer(serializers.ModelSerializer):
    working_days = WorkingDaySerializer(many=True)

    class Meta:
        model = WorkPlan
        fields = ['id', 'working_days']


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    work_plan = WorkPlanSerializer(read_only=True, many=True)
    trainer = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all())

    class Meta:
        model = Reservation
        fields = ['user', 'trainer', 'date', 'start_time', 'end_time', 'work_plan']




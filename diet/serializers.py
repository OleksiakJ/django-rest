from django.db.models import Sum
from rest_framework import serializers
from .models import Meal, Dishes, Diet
from coach.serializers import TrainerSerializer
from user.serializers import UserSerializer

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('meal_number', 'hour', 'calories', 'protein', 'carbs', 'fats', 'recipe')

class DishesSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Dishes
        fields = ('days', 'meals')

class DietSerializer(serializers.ModelSerializer):
    dishes = DishesSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)

    total_calories = serializers.SerializerMethodField()
    total_protein = serializers.SerializerMethodField()
    total_carbs = serializers.SerializerMethodField()
    total_fats = serializers.SerializerMethodField()

    class Meta:
        model = Diet
        fields = ('name_diet', 'dishes', 'user', 'trainer', 'description_diet', 'total_calories', 'total_protein', 'total_carbs', 'total_fats')

    def get_total_calories(self, obj):
        return self.get_total_per_day(obj, 'meals__calories')

    def get_total_protein(self, obj):
        return self.get_total_per_day(obj, 'meals__protein')

    def get_total_carbs(self, obj):
        return self.get_total_per_day(obj, 'meals__carbs')

    def get_total_fats(self, obj):
        return self.get_total_per_day(obj, 'meals__fats')

    def get_total_per_day(self, obj, field):
        totals_per_day = obj.dishes.values('days').annotate(total=Sum(field))
        return {entry['days']: entry['total'] for entry in totals_per_day}

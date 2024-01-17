from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealViewSet, DishesViewSet, DietViewSet, UserDietView


router = DefaultRouter()
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'dishes', DishesViewSet, basename='dishes')
router.register(r'diets', DietViewSet, basename='diet')

urlpatterns = [
    path('', include(router.urls)),
    path('user-diet/', UserDietView.as_view(), name='user-diet'),
]
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Meal, Dishes, Diet
from .serializers import MealSerializer, DishesSerializer, DietSerializer

class MealViewSet(viewsets.ModelViewSet):
    """CRUD for Meal. Only for admin user"""
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Meal.objects.all()

class DishesViewSet(viewsets.ModelViewSet):
    """CRUD for Dishes. Only for admin user"""
    serializer_class = DishesSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Dishes.objects.all()

class DietViewSet(viewsets.ModelViewSet):
    """CRUD for Diet. Only for admin user"""
    serializer_class = DietSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Diet.objects.all()


class UserDietView(generics.ListAPIView):
    serializer_class = DietSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Diet.objects.filter(user=user)
        queryset = queryset.prefetch_related('dishes__meals')


        return queryset

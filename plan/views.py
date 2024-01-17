from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import TrainingPlan, Exercise, ExerciseSet
from .serializers import TrainingPlanSerializer, ExerciseSerializer, ExerciseSetSerializer



class ExerciseViewSet(viewsets.ModelViewSet):
    """CRUD for Exercise. Only for admin user"""
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Exercise.objects.all()


class ExerciseSetViewSet(viewsets.ModelViewSet):
    """CRUD for ExerciseSet. Only for admin user"""
    serializer_class = ExerciseSetSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = ExerciseSet.objects.all()


class TrainingPlanViewSet(viewsets.ModelViewSet):
    """CRUD for TrainingPlan. Only for admin user"""
    serializer_class = TrainingPlanSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = TrainingPlan.objects.all()


class UserTrainingPlanListView(generics.ListAPIView):
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = TrainingPlan.objects.filter(user=user)
        queryset = queryset.prefetch_related('exercise_set__exercises')

        return queryset


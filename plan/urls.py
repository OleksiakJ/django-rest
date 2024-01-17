from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, ExerciseSetViewSet, TrainingPlanViewSet, UserTrainingPlanListView

app_name = 'plan'

router = DefaultRouter()
router.register(r'exercise', ExerciseViewSet, basename='exercise')
router.register(r'exerciseset', ExerciseSetViewSet, basename='exerciseset')
router.register(r'trainingplan', TrainingPlanViewSet, basename='treainingplan')

urlpatterns = [
    path('', include(router.urls)),
    path('user-training-plans/', UserTrainingPlanListView.as_view(), name='user-training-plans'),
]



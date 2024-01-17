from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import RatingCreateView, RatingAdminViewSet, TrainerView, TrainerViewAdmin, AllTrainersView

router = SimpleRouter()
router.register(r'rating', RatingAdminViewSet, basename='')
router.register(r'trainer', TrainerViewAdmin, basename='')

app_name = 'coach'

urlpatterns = [
    path('rating/create/', RatingCreateView.as_view(), name='create_rate_trainer'),
    path('trainers/', AllTrainersView.as_view(), name='all_trainers'),
    path('', include(router.urls)),  # /coach/rating/ i /coach/trainer/
    path('trainer/<int:trainer_id>/rating', TrainerView.as_view(), name='trainer_rating'),
]

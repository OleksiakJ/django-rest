from django.urls import path
from .views import ReservationListCreateView, TrainerWorkPlanView, CancelReservationView, TrainerReservationsView

app_name = 'meet'

urlpatterns = [
    path('trainer/<int:trainer_id>/reservation/', ReservationListCreateView.as_view(), name='trainer-reservation'),
    path('trainer/<int:trainer_id>/reservations/', TrainerReservationsView.as_view(), name='trainer-reservations'),
    path('trainer/<int:trainer_id>/reservation/<int:reservation_id>/cancel/', CancelReservationView.as_view(),name='cancel-reservation'),
    path('trainer/<int:trainer_id>/workplan/', TrainerWorkPlanView.as_view(), name='trainer-workplan'),
]

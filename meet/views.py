from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer, WorkPlanSerializer
from .models import WorkPlan



class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        trainer_id = self.kwargs['trainer_id']
        serializer.save(user=user, trainer_id=trainer_id)


class TrainerReservationsView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        trainer_id = self.kwargs['trainer_id']
        return Reservation.objects.filter(trainer_id=trainer_id)


class CancelReservationView(generics.DestroyAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'reservation_id'

    def get_queryset(self):
        user = self.request.user
        trainer_id = self.kwargs.get('trainer_id')
        return Reservation.objects.filter(user=user, trainer_id=trainer_id)

    def get_object(self):
        queryset = self.get_queryset()
        lookup_value = self.kwargs.get(self.lookup_url_kwarg)
        return generics.get_object_or_404(queryset, id=lookup_value)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class TrainerWorkPlanView(generics.RetrieveAPIView):
    serializer_class = WorkPlanSerializer
    lookup_field = 'trainer_id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        trainer_id = self.kwargs['trainer_id']
        return WorkPlan.objects.filter(trainer__id=trainer_id)


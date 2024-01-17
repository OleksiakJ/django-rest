from rest_framework import viewsets, generics, status
from django.db.models import Avg, Count, Q
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Trainer, Rating
from coach.serializers import TrainerSerializer, RatingSerializer


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        trainer_id = self.request.data.get('trainer')
        rating_value = self.request.data.get('rating_value')
        comments = self.request.data.get('comments')
        existing_rating = Rating.objects.filter(user_added=self.request.user, trainer_id=trainer_id).first()

        if existing_rating:
            existing_rating.delete()

        serializer.save(
            user_added=self.request.user,
            trainer_id=trainer_id,
            rating_value=rating_value,
            comments=comments
        )



class TrainerView(generics.ListAPIView):
    ''' Ratings view for a specific trainer'''
    serializer_class = RatingSerializer

    def get_queryset(self):
        trainer_id = self.kwargs['trainer_id']
        queryset = Rating.objects.filter(trainer_id=trainer_id)
        return queryset

    def get(self, request, *args, **kwargs):
        trainer_id = self.kwargs['trainer_id']
        ratings = Rating.objects.filter(trainer_id=trainer_id)
        average_rating = ratings.aggregate(Avg('rating_value'))['rating_value__avg']
        total_votes = ratings.aggregate(Count('rating_value'))['rating_value__count']

        if average_rating is not None:
            response_data = {
                'average_rating': round(average_rating, 2),
                'total_votes': total_votes,
                'ratings': RatingSerializer(ratings, many=True).data
            }
        else:
            response_data = {
                'average_rating': None,
                'total_votes': 0,
                'ratings': RatingSerializer(ratings, many=True).data
            }

        return Response(response_data)


class AllTrainersView(generics.ListAPIView):
    """List all trainers"""
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    def get_queryset(self):
        queryset = Trainer.objects.all()

        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(surname__icontains=search_query)
            )

        min_rating = self.request.query_params.get('min_rating', None)
        if min_rating is not None:
            queryset = queryset.annotate(avg_rating=Avg('trainer_ratings__rating_value'))
            queryset = queryset.filter(avg_rating__gte=min_rating)

        min_votes = self.request.query_params.get('min_votes', None)
        if min_votes is not None:
            queryset = queryset.annotate(num_votes=Count('trainer_ratings'))
            queryset = queryset.filter(num_votes__gte=min_votes)

        return queryset




class TrainerViewAdmin(viewsets.ModelViewSet):
    """CRUD for trainers. Only for admin user"""
    serializer_class = TrainerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Trainer.objects.all()


class RatingAdminViewSet(viewsets.ModelViewSet):
    """Admin CRUD for ratings"""
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )



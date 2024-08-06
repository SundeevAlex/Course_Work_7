from rest_framework import generics
from habits.serializers import HabitsSerializer


class HabitsCreateApiView(generics.CreateAPIView):
    serializer_class = HabitsSerializer

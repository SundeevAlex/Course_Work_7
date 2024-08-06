from rest_framework import generics

from habits.models import Habits
from habits.serializers import HabitsSerializer


class HabitsCreateApiView(generics.CreateAPIView):
    serializer_class = HabitsSerializer


class HabitsUpdateApiView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer


class HabitsDestroyApiView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

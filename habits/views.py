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


class HabitsPublicListApiView(generics.ListAPIView):
    """Вывод списока публичных привычек"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()

    def get_queryset(self):
        queryset = Habits.objects.filter(is_published=True)
        return queryset


class HabitsListApiView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

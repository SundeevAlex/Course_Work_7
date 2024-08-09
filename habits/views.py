from rest_framework import generics

from habits.models import Habits
from habits.paginations import HabitsListPagination
from habits.permissions import IsCreator
from habits.serializers import HabitsSerializer


class HabitsCreateApiView(generics.CreateAPIView):
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        """Делаем пользователя автором привычки."""
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitsUpdateApiView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    permission_classes = (IsCreator,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habits.objects.filter(owner=user)


class HabitsDestroyApiView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsCreator,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habits.objects.filter(owner=user)


class HabitsPublicListApiView(generics.ListAPIView):
    """Вывод списока публичных привычек"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitsListPagination

    def get_queryset(self):
        queryset = Habits.objects.filter(is_published=True)
        return queryset


class HabitsListApiView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsListPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habits.objects.all()
        elif user.is_authenticated:
            return Habits.objects.filter(owner=user)

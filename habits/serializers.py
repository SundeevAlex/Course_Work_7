from rest_framework import serializers
from habits.models import Habits


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор модели Habits."""

    class Meta:
        model = Habits
        fields = "__all__"

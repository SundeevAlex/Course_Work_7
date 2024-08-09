from rest_framework import serializers

from habits.models import Habits
from habits.validators import (CombinationValidator, DurationValidator,
                               FrequencyValidator,
                               NotConnectionHabitAndRewardValidator,
                               NotRewardOrConnectionHabitValidator)


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор модели Habits."""

    class Meta:
        model = Habits
        fields = "__all__"

        validators = [
            NotConnectionHabitAndRewardValidator("connection_habit", "reward"),
            DurationValidator("duration"),
            CombinationValidator("connection_habit", "habit_is_pleasant"),
            NotRewardOrConnectionHabitValidator(
                "habit_is_pleasant", "connection_habit", "reward"
            ),
            FrequencyValidator("number_of_executions"),
        ]

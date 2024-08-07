from rest_framework.serializers import ValidationError


class NotConnectionHabitAndRewardValidator:
    """Исключить одновременный выбор связанной привычки и указания вознаграждения."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habits):
        if habits.get('connection_habit') and habits.get('reward'):
            raise ValidationError('Связанную привычку и вознаграждение нельзя выбирать одновременно!')


class DurationValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habits):
        if habits.get('duration') > 120:
            raise ValidationError('Это действие можно выполняеть не более двух минут!')


class CombinationValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habits):
        if habits.get('connection_habit'):
            if not habits.get('habit_is_pleasant'):
                raise ValidationError('Приятными могут быть только связанные привычки!')


class NotRewardOrConnectionHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, habits):
        if habits.get('habit_is_pleasant'):
            if habits.get('connection_habit') or habits.get('reward'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки!')


class FrequencyValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habits):
        numbers_list = [1, 2, 3, 4, 5, 6, 7]
        number = habits.get('number_of_executions')
        try:
            number in numbers_list
        except ValidationError:
            print('Нельзя выполнять привычку реже, чем 1 раз в 7 дней!')

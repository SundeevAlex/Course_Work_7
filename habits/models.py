from datetime import timedelta

from django import forms
from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Место выполнения"
    )
    time = models.TimeField(**NULLABLE, verbose_name="Время выполнения")
    action = models.CharField(max_length=100, verbose_name="Действие")
    habit_is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Связанная привычка"
    )
    number_of_executions = models.IntegerField(
        default=7, verbose_name="Периодичность (в днях) - от 1 до 7"
    )
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.DurationField(
        default=timedelta(seconds=120), verbose_name="Время на выполнение (в минутах)"
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return (
            f"Я буду {self.action} в {self.time} в {self.place}. Автор: {self.owner}."
        )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

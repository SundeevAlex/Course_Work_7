from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="proba@sky.com")
        self.client.force_authenticate(user=self.user)

        self.habits = Habits.objects.create(
            owner=self.user,
            place="Home",
            time="15:00:00",
            action="Sleep",
            habit_is_pleasant=True,
            connection_habit=None,
            number_of_executions=3,
            reward="Relax",
            duration=timedelta(seconds=120),
            is_published=True,
        )

    def test_habits_create(self):
        """Тест создания привычки."""

        url = reverse("habits:habits_create")
        data = {
            "action": "Run!",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "action": "Run!",
                "connection_habit": None,
                "duration": "00:02:00",
                "habit_is_pleasant": False,
                "id": 2,
                "is_published": False,
                "number_of_executions": 1,
                "owner": 1,
                "place": None,
                "reward": None,
                "time": None,
            },
        )
        self.assertTrue(Habits.objects.all().exists())

    def test_habits_update(self):
        """Тест изменения привычки."""

        url = reverse("habits:habits_update", args=(self.habits.pk,))
        data = {
            "reward": "Stop!",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "Stop!")

    def test_habits_delete(self):
        """Тест удаления привычки."""

        url = reverse("habits:habits_delete", args=(self.habits.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)

    def test_habits_public_list(self):
        """Тест вывода списка публичных привычек."""

        url = reverse("habits:public_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_habits_list(self):
        """Тест вывода списка привычек."""

        url = reverse("habits:habits_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

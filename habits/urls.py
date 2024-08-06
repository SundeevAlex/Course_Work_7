from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitsCreateApiView


app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitsCreateApiView.as_view(), name="habits_create"),

]

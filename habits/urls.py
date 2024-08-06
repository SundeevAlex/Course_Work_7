from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitsCreateApiView, HabitsUpdateApiView, HabitsDestroyApiView


app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitsCreateApiView.as_view(), name="habits_create"),
    path("habits/update/<int:pk>/", HabitsUpdateApiView.as_view(), name="habits_update"),
    path("habits/delete/<int:pk>/", HabitsDestroyApiView.as_view(), name="habits_delete"),

]

import datetime

from celery import shared_task

from habits.models import Habits
from habits.services import send_telegram_message


@shared_task
def tg_send_message():
    timestamp = str(datetime.datetime.now().strftime("%H:%M"))
    habits = Habits.objects.all()

    for habit in habits:
        if str(habit.time)[0:5] == timestamp:
            tg_chat = habit.owner.chat_id
            if tg_chat:
                executions = habit.number_of_executions
                if executions != 0:
                    message = f"Я буду {habit.action} в {habit.time} в {habit.place}."
                    send_telegram_message(tg_chat, message)
                    executions -= 1
                    habit.save()

from celery import shared_task
from django.core.mail import send_mail

from users.models import User
import datetime
import pytz


@shared_task
def hi():
    print("HELLO")

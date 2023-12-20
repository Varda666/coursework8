from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

from users.models import User
from telebot import TeleBot


bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

@shared_task
def send_message_telegram(chat_id, text):
    bot.send_message(chat_id=settings.MY_CHAT_ID, text=text)


# @shared_task
# def check_last_visit(pk):
#     instance = User.objects.filter(pk=pk).first
#     days_after_last_visit = datetime.date.today() - instance.last_visit
#     if days_after_last_visit > 30:
#         return False
#     return True






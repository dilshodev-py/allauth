import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AllAuth.settings')
django.setup()
from django.contrib.auth.models import User

import telebot

bot = telebot.TeleBot("7845874862:AAGoP78o_YlrvHbVmXcKo6b2bxhSWsy8HVU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	for user in User.objects.all():
		bot.send_message(message, f"Howdy, how are you doing? {user.username}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()



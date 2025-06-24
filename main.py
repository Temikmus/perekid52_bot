# -*- coding: utf-8 -*-
import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    id_user = message.chat.id
    username = message.from_user.username
    bot.send_message(id_user, f'Привет, <b>{username}</b>! 👋\n',
                      parse_mode='HTML')


bot.polling(none_stop=True)

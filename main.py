# !/usr/bin/python3
# -*- coding: utf-8 -*-

import telebot, os
from dotenv import load_dotenv

# Загрузка токена для телеграм-бота
load_dotenv()
TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Бот, написанный Золотаревым Максимом, для выполнения тестового задания для Alef Development.")


@bot.message_handler(commands=['commands'])
def send_welcome(message):
    bot.reply_to(message, "/start, /help - приветствие. \n/commands - доступные команды. \n/parse - пропарсить сайт и "
                          "обновить базу данных.")


# @bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['parse'])
def parsing(message):
    bot.send_message(message.chat.id, 'Запуск парсинга...')


bot.infinity_polling()
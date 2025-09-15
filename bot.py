import os
import telebot

TOKEN = "7647076911:AAHQsdNL2aoL4Rv0uSkPn9fPl4QFX1gbZTM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот и я запущен ??")

@bot.message_handler(func=lambda m: True)
def echo_message(message):
    bot.send_message(message.chat.id, f"Ты сказал: {message.text}")

print("Бот запущен и работает!")
bot.polling(non_stop=True)
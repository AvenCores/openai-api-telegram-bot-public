import openai
import telebot
from telebot import types
from datetime import datetime
from sys import platform

from botapiconfig import openaiapi, telegrambotapi

openai.api_key = openaiapi
bot = telebot.TeleBot(telegrambotapi)


def mainstarter():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.InlineKeyboardButton("Мои проекты")
        button2 = types.InlineKeyboardButton("Поддержать автора монетой")
        button3 = types.InlineKeyboardButton("Техническая поддержка")
        button4 = types.InlineKeyboardButton("Исходный код")
        button5 = types.InlineKeyboardButton("Статус бота")
        markup.add(button1, button2, button3, button4, button5)
        sticker = open("sticker.webp", "rb")
        bot.send_sticker(message.chat.id, sticker)
        markdown = """Привет друг! \nДанный телеграм бот основан на технологии ChatGPT. \nОтвет придется ждать довольно долго. \n\n*Что такое ChatGPT?*\nChatGPT - это модель языкового обработки, разработанная OpenAI. Она была обучена на множестве текстов и может генерировать тексты, отвечать на вопросы и выполнять другие задачи обработки языка.\n\n*Как задать вопрос ChatGPT?*\nЛегко! Просто напиши свой вопрос и ожидай ответа."""
        bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == "мои проекты":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Группа VK", url="https://vk.com/chatgptcontent")
            button2 = types.InlineKeyboardButton("Telegram канал", url="https://t.me/hzfnews")
            markup.add(button1, button2)
            markdown = "*Нажми на кнопку!*"
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "поддержать автора монетой":
            markdown = """*QIWI*: [Нажми на меня](https://qiwi.com/n/AVENCORESDONATE)\n*Сбер*: `2202 2050 7215 4401`\n*ВТБ*: `2200 2404 1001 8580`"""
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "техническая поддержка":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Я в VK", url="https://vk.com/avencores")
            button2 = types.InlineKeyboardButton("Я в Telegram", url="https://t.me/avencores")
            markup.add(button1, button2)
            markdown = "*Нажми на кнопку!*"
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "статус бота":
            markdown = datetime.now().strftime(f"""*Бот работает в штатном режиме.*\n
*Время*: %H:%M:%S
*Дата*: %d.%m.%y

*Система*: {platform}""")
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "исходный код":
            bot.send_message(message.chat.id, "https://github.com/AvenCores/chatgpt-telegram-bot-public")

        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                max_tokens=500,
                temperature=0,
                top_p=0,
            )
            bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])

    bot.polling(none_stop=True)


while True:
    try:
        mainstarter()
    except Exception:
        continue

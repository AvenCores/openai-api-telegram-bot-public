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
            markdown = """*Подпишись на нашу группу и канал*

Мы будем рады видеть вас в нашей группе ВКонтакте и канале в Telegram! Там вы сможете узнать о наших новостях, анонсах и мероприятиях, а также общаться с другими пользователями.

Подпишитесь на оба канала, чтобы быть в курсе всех новостей и обновлений, связанных с нашим ботом.

Благодарим за использование нашего бота!"""
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "поддержать автора монетой":
            markdown = """ *Поддержать проект*

Если вам нравится использовать этот бот и вы хотите поддержать наш проект, мы будем очень благодарны за любую помощь.

Вы можете сделать донат нашему проекту через следующие платежные системы:

*QIWI*: [Нажми на меня](https://qiwi.com/n/AVENCORESDONATE)
*Сбер*: `2202 2050 7215 4401`
*ВТБ*: `2200 2404 1001 8580`

Ваша поддержка поможет нам продолжать развивать этот бот и добавлять новые функции.

Благодарим за использование нашего бота и за вашу поддержку!"""
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "техническая поддержка":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Я в VK", url="https://vk.com/avencores")
            button2 = types.InlineKeyboardButton("Я в Telegram", url="https://t.me/avencores")
            markup.add(button1, button2)
            markdown = """*Техническая поддержка*

Если у вас возникли проблемы с использованием этого бота или у вас есть вопросы по поводу его функциональности, наша команда технической поддержки всегда готова помочь вам.

Вы можете связаться с нами через наши страницы в социальных сетях, для этого просто нажмите на кнопки снизу.

Мы гарантируем быстрый и профессиональный ответ на все ваши запросы.

Благодарим за использование нашего бота!"""
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "статус бота":
            markdown = datetime.now().strftime(f"""*Бот работает в штатном режиме.*\n
*Время на сервере*: %H:%M:%S
*Дата на сервере*: %d.%m.%y

*Система на сервере*: {platform}""")
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "исходный код":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("GitHub Page",
                                                 url="https://github.com/AvenCores/chatgpt-telegram-bot-public")
            button2 = types.InlineKeyboardButton("Full GNU GPL V3",
                                                 url="https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
            markdown = """⚠️ *Предупреждение* ⚠️

Данный телеграм бот распространяется под лицензией GNU GPL 3. Это означает, что вы имеете право свободно использовать, распространять и изменять исходный код этого бота, при условии, что все ваши изменения также будут распространяться под той же лицензией.

Мы просим вас уважать авторские права и не использовать этот бот в незаконных целях. Если вы не согласны с условиями GNU GPL 3, пожалуйста, прекратите использование этого бота немедленно.

Спасибо за понимание и уважение к правам авторов!"""
            markup.add(button1, button2)
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        else:
            msg = bot.send_message(message.chat.id, "📄Идет загрузка, подождите...")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                max_tokens=2000,
                temperature=0,
                top_p=0,
            )
            bot.edit_message_text("✅Ответ получен!", chat_id=message.chat.id, message_id=msg.message_id)
            bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])

    bot.polling(none_stop=True)


while True:
    try:
        mainstarter()
    except Exception:
        continue

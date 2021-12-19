import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)

# Начало диалога
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')
    dbworker.set(message.chat.id, config.States.STATE_NAME.value)
    bot.send_message(message.chat.id, 'Как к тебе можно обращаться?')

    # По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
    @bot.message_handler(commands=['reset'])
    def cmd_reset(message):
        bot.send_message(message.chat.id, 'Напомни, пожалуйста...')
        dbworker.set(message.chat.id, config.States.STATE_NAME.value)
        bot.send_message(message.chat.id, 'Как к тебе можно обращаться?')

# Обработка ввода имени
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_NAME.value)
def user_name(message):
    text = message.text
    if not text.isalpha():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Кажется, ты не ввел имя!')
        return
    else:
        bot.send_message(message.chat.id, f'У тебя красивое имя! Приятно познакомиться, {text})')
        # Меняем текущее состояние
        dbworker.set(message.chat.id, config.States.STATE_NAME.value)
        # Сохраняем имя
        dbworker.set((message.chat.id, config.States.STATE_NAME.value), text)
        bot.send_message(message.chat.id, 'Скажи, пожалуйста, свой возраст!')
        dbworker.set(message.chat.id, config.States.STATE_AGE.value)

# Обработка вызраста
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_AGE.value)
def user_age(message):
    text = message.text
    if not text.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Скажи правду!')
        return
    elif int(message.text) < 5 or int(message.text) > 90:
        bot.send_message(message.chat.id, "Хмм... Какой-то странный возраст. Отвечай честно!")
        return
    else:
        bot.send_message(message.chat.id, f'Супер, {text}, значит {text}')
        # Меняем текущее состояние
        dbworker.set(message.chat.id, config.States.STATE_OPERATION.value)
        # Сохраняем число
        dbworker.set((message.chat.id, config.States.STATE_AGE.value), text)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Посоветуй книгу')
        itembtn2 = types.KeyboardButton('Хочу послушать музыку')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, 'Выберите, пожалуйста, чтобы ты хотел сделать', reply_markup=markup)

# Выбор действия
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_OPERATION.value)
def operation(message):
    # Текущее действие
    op = message.text

    if op == 'Посоветуй книгу':
        bot.send_message(message.chat.id,
                         "https://librebook.me/harry_potter_and_the_sorcerer_s_stone/vol1/1"
                         "Хорошая книга,прочти обязательно!")
        bot.send_message(message.chat.id,
                         "Наслаждайся! Если захочешь пообщаться снова - "
                         "отправь команду /start.")
    elif op == 'Хочу послушать музыку':
        bot.send_message(message.chat.id,
                         "Здорово! Попробуй вот это"
                         "https://open.spotify.com/playlist/37i9dQZF1DWU0r6G8OGirN?si=inn5wxqtRHSoNuBML4Yagg"
                         "С тобой очень приятно иметь дело. Если захочешь пообщаться снова - "
                         "отправь команду /start.")
        dbworker.set(message.chat.id, config.States.STATE_START.value)



if __name__ == '__main__':
    bot.infinity_polling()
import telebot

token = '5043369834:AAFkYHEb1SLm3vu1AzH9yxPKlK_MiBlc4ds'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Отлично', 'Плохо')
    bot.send_message(message.chat.id, 'Привет!Как дела?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, 'Это очень хорошо!')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Что ни делается, все к лучшему!')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Напиши /start')
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start', '/help')
        bot.send_message(message.chat.id, 'Если тебе нужна помощь, нажми или напиши /help, если нет - нажми /start', reply_markup=keyboard)


bot.polling()
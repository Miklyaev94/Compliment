from select_compliment import select_compliment
import telebot
import time
token='Введи свой'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Зай, если тебе хочется комплимен, то просто скажи : "да"')
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message):
#    bot.send_message(message.chat.id, select_compliment())
#time.sleep(5)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'да':
        bot.send_message(message.from_user.id, select_compliment())
    elif message.text == 'нет':
        bot.send_message(message.from_user.id, 'Хорошо, пока не буду говорить')
    else:
        bot.reply_to(message, 'Это что такое? Введи "да" если хочешь комплимент')


bot.polling()


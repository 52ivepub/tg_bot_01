import telebot
import webbrowser
bot = telebot.TeleBot("7672525355:AAE-TEINCA5rdlFbxIkXvHJvdri15lfY6zg")



@bot.message_handler(commands=['start', 'main', 'hello'])
def  main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, {message.from_user.username}')


@bot.message_handler(commands=['help'])
def  main(message):
    bot.send_message(message.chat.id, "<b>Чем</b> <em><u>могу помочь ?</u></em>", parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open_new('https://novosibirsk.drom.ru/')



bot.polling(none_stop=True)




import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot("7672525355:AAE-TEINCA5rdlFbxIkXvHJvdri15lfY6zg")


@bot.message_handler(commands=['start'])
def start(message):
    """Эхо бот"""
    bot.send_message(message.chat.id, f'Привет  😊')
    markup = types.ReplyKeyboardMarkup()
    btn1 =types.KeyboardButton("Перейти на сайт", )
    
    markup.row(btn1)
    btn2 = types.KeyboardButton("Удалить фото")
    btn3 = types.KeyboardButton("Изменить текст")
    markup.add(btn2, btn3)
    file = open("./photo_01.jpg", 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.send_audio(message.chat.id, file, reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, "Website is open")
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, "Delete")




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == "edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


@bot.message_handler(content_types=['photo',])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 =types.InlineKeyboardButton("Перейти на сайт", url='https://europaplus.ru/programs/top40')
    
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("Изменить текст", callback_data='edit')
    markup.add(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup) 




    


bot.polling(none_stop=True)
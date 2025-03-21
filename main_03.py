import telebot
import requests
import json

bot = telebot.TeleBot("7672525355:AAE-TEINCA5rdlFbxIkXvHJvdri15lfY6zg")
API = 'd4caf08186cd9d2e731ea09ddb14723e'
x = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
y = 'https://api.openweathermap.org/data/2.5/weather?q={London}&appid={d4caf08186cd9d2e731ea09ddb14723e}'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет рад тебя видеть, Напиши название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    """Бот о погоде"""
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:    
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас погода: {temp }')
        image = "sun.jpg" if temp > 5.0 else 'cloud.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан неверно')





bot.polling(none_stop=True)
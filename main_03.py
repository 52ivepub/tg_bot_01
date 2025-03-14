import telebot

bot = telebot.TeleBot("7672525355:AAE-TEINCA5rdlFbxIkXvHJvdri15lfY6zg")
API = 'd4caf08186cd9d2e731ea09ddb14723e'
x = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
y = 'https://api.openweathermap.org/data/2.5/weather?q={London}&appid={d4caf08186cd9d2e731ea09ddb14723e}'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет рад тебя видеть, Напиши название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()



bot.polling(none_stop=True)
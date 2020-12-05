import os
import telebot
import urllib
import json
import ASUS.GPIO as GPIO

pir = 26

 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)


bot = telebot.TeleBot("1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII")


@bot.message_handler(commands=['inicio', 'soc'])
def send_start_message(message):
    while True:
        if GPIO.input(pir) == GPIO.HIGH:
            bot.reply_to(message, "Sensor ativado!")
        

@bot.message_handler(commands=['people'])
def send_people(message):
    bot.reply_to(message, get_reply_message())


def get_reply_message():
    n_people, people = get_people()
    message = "Existem " \
              + str(n_people) + \
              " pessoas no espaço neste momento, são elas: \n\n"
    for person in people:
        message += person["name"] + \
                   " na espaçonave " + person["craft"] + "\n\n"

    return message


def get_people():
    req = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    return obj["number"], obj["people"]


bot.polling()

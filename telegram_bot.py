import os
import telepot
import urllib
import json
import ASUS.GPIO as GPIO

pir = 26

 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)


bot = telepot.Bot("1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == 'On':
        while True:

            if GPIO.input(pir) == GPIO.HIGH:
                bot.sendMessage(chat_id, "Sensor ativado!")


bot.message_loop(handle)                

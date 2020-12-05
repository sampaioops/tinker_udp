import os
import telepot
import urllib
import json
import time
import ASUS.GPIO as GPIO

pir = 26

 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)



def handle(msg):
    print('teste')
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == 'Ativa Sensor':
        while True:
            
            if command == 'break':
                break
            
            if GPIO.input(pir) == GPIO.HIGH:
                bot.sendMessage(chat_id, "Sensor ativado!")


bot = telepot.Bot('1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII')
bot.message_loop(handle)            

while 1:
    time.sleep(10)
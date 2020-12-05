import os
import telepot
import urllib
import json
import time
import ASUS.GPIO as GPIO
from threading import Thread 

pir = 26

 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)

iniciaSensor = False

def executaSensor(chat_id):
    while iniciaSensor:
        if GPIO.input(pir) == GPIO.HIGH:
            bot.sendMessage(chat_id, "Sensor ativado!")

def handle(msg):
    
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == 'start sensor':
        iniciaSensor = True
        t = Thread(target = executaSensor, args =(chat_id, )) 
        t.start()
    elif command == 'stop sensor':
        iniciaSensor = False
            


bot = telepot.Bot('1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII')
bot.message_loop(handle)            

while 1:
    time.sleep(10)
import os
import telepot
import urllib
import json
import time
import ASUS.GPIO as GPIO
from threading import Thread 

class CountdownTask: 
      
    def __init__(self): 
        self._running = True

    def start(self):
        self._running = True
      
    def terminate(self): 
        self._running = False
      
    def run(self, chat_id): 
        while self._running: 
            if GPIO.input(pir) == GPIO.HIGH:
                bot.sendMessage(chat_id, "Sensor ativado!")

pir = 26

ledRed = 37
ledBlue = 35

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

c = CountdownTask()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == 'start sensor':
        c.start()
        t = Thread(target = c.run, args =(chat_id, )) 
        t.start() 
    elif command == 'stop sensor':
        c.terminate()
    elif command == 'play red':
         GPIO.output(ledRed, 1)
         time.sleep(0.5)
    elif command == 'stop red':	
         GPIO.output(ledRed, 0)
    elif command == 'play blue':	
         GPIO.output(ledBlue, 1)
    elif command == 'stop blue':	
         GPIO.output(ledBlue, 0)
            

bot = telepot.Bot('1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII')
bot.message_loop(handle)            

while 1:
    time.sleep(10)


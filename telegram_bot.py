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
        self._blink = True

    def start(self):
        self._running = True
      
    def terminate(self): 
        self._running = False
      
    def run(self, chat_id): 
        while self._running: 
            if GPIO.input(pir) == GPIO.HIGH:
                bot.sendMessage(chat_id, "Movimento detectado!!")
                time.sleep(1)
    
    def run_blink(self):
        count = 0
        while self._blink:
            
            if count == 0:
                 GPIO.output(ledRed, 1)
                 GPIO.output(ledBlue, 0)
                 time.sleep(0.5)
                 count = 1
            elif count == 1:
                 GPIO.output(ledRed, 0)
                 GPIO.output(ledBlue, 1)
                 time.sleep(0.5)
                 count = 0

    def start_blink(self):
        self._blink = True

    def terminate_blink(self):
        self._blink = False



    def play_red(self):
         GPIO.output(ledRed, 1)

    def stop_red(self):
         GPIO.output(ledRed, 0)

    def play_blue(self):
         GPIO.output(ledBlue, 1)

    def stop_blue(self):
         GPIO.output(ledBlue, 0)

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
    print(chat_id)
    command = msg['text']

    if command == 'commands':
        bot.sendMessage(chat_id, "Segue os comandos seguintes: \n 1.start sensor \n 2.stop sensor \n 3.play red \n 4.stop red \n 5.play blue \n 6.stop blue \n 7.start blink \n 8.stop blink")

    elif command == 'start sensor':
        c.start()
        t = Thread(target = c.run, args =(chat_id, )) 
        t.start() 
    elif command == 'stop sensor':
        c.terminate()
    elif command == 'play red':
         c.play_red()
    elif command == 'stop red':	
         c.stop_red()
    elif command == 'play blue':	
         c.play_blue()
    elif command == 'stop blue':	
         c.stop_blue()
    elif command == 'start blink':
        c.start_blink()
        t = Thread(target = c.run_blink) 
        t.start()
    elif command == 'stop blink':
        c.terminate_blink()
            

bot = telepot.Bot('1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII')

bot.message_loop(handle)            

while 1:
    time.sleep(10)


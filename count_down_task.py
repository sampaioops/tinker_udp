import time
import os
import telepot
import urllib
import json
import time
import ASUS.GPIO as GPIO


class CountdownTask: 

    def __init__(self): 
        self._running = True

pir = 26

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pir, GPIO.IN)
      
def terminate(self): 
    self._running = False
      
def run(self): 
    while self._running: 
        while True:
            
            if command == 'break':
                break
            
            if GPIO.input(pir) == GPIO.HIGH:
                bot.sendMessage(chat_id, "Sensor ativado!")
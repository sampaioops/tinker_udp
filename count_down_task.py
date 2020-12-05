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
      
def run(self, chat_id, bot): 
    while self._running: 
        if GPIO.input(pir) == GPIO.HIGH:
            bot.sendMessage(chat_id, "Sensor ativado!")
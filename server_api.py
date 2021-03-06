import ASUS.GPIO as GPIO
import socket
import time
from datetime import datetime


localIP     = "192.168.18.6"
localPort   = 20001
bufferSize  = 1024
 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
  
ledRed = 37
ledBlue = 35

pir = 26

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    message, address = UDPServerSocket.recvfrom(bufferSize)

    print(message.decode('utf-8'))

    if GPIO.input(pir) == GPIO.HIGH:
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        UDPServerSocket.sendto(str.encode('SENSOR ATIVADO! - ' + data_e_hora_em_texto), address)
    else:
        UDPServerSocket.sendto(str.encode(''), address)


    #if message.decode('utf-8') == 'play red':
    #     GPIO.output(ledRed, 1)
    #     time.sleep(0.5)
    #     UDPServerSocket.sendto(str.encode('Red on!'), address)
    #elif message.decode('utf-8') == 'stop red':	
    #     GPIO.output(ledRed, 0)
    #     UDPServerSocket.sendto(str.encode('Red off!'), address)
    #elif message.decode('utf-8') == 'play blue':	
    #     GPIO.output(ledBlue, 1)
    #     UDPServerSocket.sendto(str.encode('Blue off!'), address)
    #elif message.decode('utf-8') == 'stop blue':	
    #     GPIO.output(ledBlue, 0)
    #     UDPServerSocket.sendto(str.encode('Blue off!'), address)
    #else:
    #     UDPServerSocket.sendto(str.encode("Command invalid!"), address)
       
   




import ASUS.GPIO as GPIO
import socket
import time

localIP     = "192.168.18.6"
localPort   = 20001
bufferSize  = 1024
 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
  
ledRed = 37
ledBlue = 35

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    message, address = UDPServerSocket.recvfrom(bufferSize)

    print(message.decode('utf-8'))
    if message.decode('utf-8') == 'play red':
         GPIO.output(ledRed, 1)
         time.sleep(0.5)
         UDPServerSocket.sendto(str.encode('Red on!'), address)
    elif message.decode('utf-8') == 'stop red':	
         GPIO.output(ledRed, 0)
         UDPServerSocket.sendto(str.encode('Red off!'), address)
    elif message.decode('utf-8') == 'start blue':	
         GPIO.output(ledBlue, 0)
         UDPServerSocket.sendto(str.encode('Blue off!'), address)
    elif message.decode('utf-8') == 'stop blue':	
         GPIO.output(ledBlue, 0)
         UDPServerSocket.sendto(str.encode('Blue off!'), address)
    else:
         UDPServerSocket.sendto(str.encode("Command invalid!"), address)
       
   




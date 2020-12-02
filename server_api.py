import ASUS.GPIO as GPIO
import socket
import time
 
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
  
led = 37

GPIO.setup(led, GPIO.OUT)


localIP     = "192.168.18.6"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

messageToClient = str.encode("play red")

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    print(message.decode('utf-8'))
    if message.decode('utf-8') == 'play red':
         GPIO.output(led, 1)
         time.sleep(0.5)
    elif message.decode('utf-8') == 'stop red':	
         GPIO.output(led, 0)
    else:
        UDPServerSocket.sendto(str.encode('Command invalid'), address)

    UDPServerSocket.sendto(str.encode('Command invalid'), address)




import socket
import time
 

serverAddressPort   = ("192.168.18.6", 20001)

bufferSize          = 1024

 

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

bytesToSend = str.encode(input())
count = 0
while True:
    
    
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])


 


    bytesToSend = str.encode(input())
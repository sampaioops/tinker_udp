import socket
import time
 

serverAddressPort   = ("192.168.18.6", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#bytesToSend = str.encode(input())
count = 0
while True:
    # Send to server using created UDP socket


    
    if count == 0:
        UDPClientSocket.sendto(str.encode('play red'), serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        msg = "Message from Server {}".format(msgFromServer[0])

        print(msg)
        count = 1
    else:
        UDPClientSocket.sendto(str.encode('stop red'), serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        msg = "Message from Server {}".format(msgFromServer[0])

        print(msg)
        count = 0

    time.sleep(1)

 


   # bytesToSend = str.encode(input())
import socket
s=socket.socket(type=socket.SOCK_DGRAM)
s.bind(('',12345))
print("UDP server up and listening")
while(True):
    message,address = s.recvfrom(1024)
    clientMsg = "Message from Client:{}".format(message.decode())
    clientIP  = "Client IP Address:{}".format(address)    
    print(clientMsg)
    print(clientIP)
    s.sendto("Hello UDP Client".encode(), address)

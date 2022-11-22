import socket
serverAddressPort  = ("127.0.0.1", 12345)
c=socket.socket(type=socket.SOCK_DGRAM)
c.sendto("Hello UDP Server".encode(), serverAddressPort)
message,address = c.recvfrom(1024)
msg = "Message from Server {}".format(message.decode())
print(msg)
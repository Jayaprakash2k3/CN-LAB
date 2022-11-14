import socket
c=socket.socket()
PORT=12345
c.connect(('localhost',PORT))
name=input("Please Enter Your Name:")
c.send(name.encode())
msg=c.recv(1024).decode()
print("Message from Server:",msg)
c.close()
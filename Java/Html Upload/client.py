import socket
c=socket.socket()
PORT=12345
c.connect(('localhost',PORT))
k=open("upload.html")
data=(k.read())
while True:
    c.send(data.encode())
    c.close()
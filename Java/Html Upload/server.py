import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
k=open("download.html","w")
while True:
    c,a=s.accept()
    print("connected to ",a)
    z=c.recv(1024).decode()
    k.write(z)
    c.close()

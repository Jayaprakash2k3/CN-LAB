import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
while True:
    c,a=s.accept()
    print("connected to ",a)
    name=c.recv(1024).decode()
    c.send(f"Hey! {name} Thanks for Connecting to the Server".encode())
    print("Welcome Message has been sent")
    c.close()

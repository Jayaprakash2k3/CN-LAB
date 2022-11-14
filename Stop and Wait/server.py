import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
data=input("Enter the message to Send:")
while True:
    c,a=s.accept()
    print("connected to ",a)
    for k in data:
        c.send(k.encode())
        ack=c.recv(2).decode()
        if(ack=='1'):
            print("Acknowledement has been received")
        else:
            c.send(k.encode())
    c.send("#".encode())        # End of Packet Indicator

    c.close()

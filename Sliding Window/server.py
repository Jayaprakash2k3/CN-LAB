import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
window=[]
data=input("Enter the message to Send:")
size=int(input("Enter the Window Size:"))
if(len(data)<size):
    window=data
else:
    window=data[:size]
while True:
    c,a=s.accept()
    print("Connected to ",a)
    for k in window:
        c.send(k.encode())
        ack=c.recv(2).decode()
        if(ack=='1'):
            print("Acknowledement has been received")
        else:
            c.send(k.encode())
    c.send("#".encode())        # End of Packet Indicator

    c.close()

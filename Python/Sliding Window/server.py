import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
data=input("Enter the message to Send:")
win=int(input("Enter the Window Size:"))
count=0
sent=0
while True:
    c,a=s.accept()
    print("connected to ",a)
    while sent!=len(data):
        while count!=win and sent!=len(data):
            c.send(data[sent].encode())
            count+=1
            sent+=1
            print(f"{data[sent-1]} has been sent")
        if(sent!=len(data)-1):
            ack=c.recv(1).decode()
        else:
            ack=c.recv(win).decode()
        for k in ack:
            if(k=='1'):
                print("Acknowledement has been received")
                count-=1
            else:
                sent-=1
                count-=1
            
    c.send("#".encode())        # End of Packet Indicator

    c.close()

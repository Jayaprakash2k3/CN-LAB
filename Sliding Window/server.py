import socket
s=socket.socket()
PORT=12345
s.bind(('',PORT))
s.listen(5)
window=[]
data=[*range(int(input("Enter the Number of packets to Send:")))]
print(data)
size=int(input("Enter the Window Size:"))
while True:
    c,a=s.accept()
    while len(data)!=0:
        z=data.pop(0)
        data.send(z.encode())
        window.append(z)
        if(len(window)==size):
            while True:
                v=c.recv(1).decode()
                if(v!=''):
                    window.pop(0)
                    break
    c.close()



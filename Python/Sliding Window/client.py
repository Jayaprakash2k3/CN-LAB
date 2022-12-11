import socket
c=socket.socket()
PORT=12345
win=int(input("Enter the Window Size:"))
c.connect(('localhost',PORT))
while True:
    msg=c.recv(1).decode()
    if(msg=="#"):
        c.close()
        break
    print(f'{msg} has been received')
    if(msg!=''):
        c.send("1".encode())
    else:
        c.send("0".encode())
    print(f'ack for {msg} has been sent')


import socket
c=socket.socket()
PORT=12345
c.connect(('localhost',PORT))
while True:
    msg=c.recv(1024).decode()
    print(f'{msg} has been received')
    if(msg!=''):
        c.send("1".encode())
    else:
        c.send("0".encode())
    print(f'ack for {msg} has been sent')
    if(msg=="#"):
        break
c.close()
import socket 
s=socket.socket()
s.connect(('localhost',12345))
with open("upload.html", "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        s.sendall(bytes_read)
s.close()
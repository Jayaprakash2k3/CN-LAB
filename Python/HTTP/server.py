import socket 
import webbrowser
s=socket.socket()
s.bind(("",12345))
s.listen(5)
c,adr=s.accept()
print("Connected to Client")

with open("download.html", "wb") as f:
    while True:
        bytes_read = c.recv(1024)
        if not bytes_read:    
            break
        f.write(bytes_read)
        print("Recived:"+bytes_read.decode())
webbrowser.open("download.html")
s.close()
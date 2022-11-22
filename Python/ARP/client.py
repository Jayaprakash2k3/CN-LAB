import socket
c= socket.socket()
c.connect(("localhost",12345))
print("Connection has been Established")
print("Address Resolution Protocol")
inp=input("Enter the Logical IP Address:")
c.send(inp.encode())
out=c.recv(1024).decode()
print("The Physical Address for the Entered Logical Address Is:",out)
c.close()



    
import socket
c= socket.socket()
c.connect(("localhost",12345))
print("Connection has been Established")
print("Reverse Address Resolution Protocol")
inp=input("Enter the Physical Address(MAC) Address:")
c.send(inp.encode())
out=c.recv(1024).decode()
print("The Logical Address for the Entered Physical Address Is:",out)
c.close()



    
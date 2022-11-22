import socket
s= socket.socket()
ARP_TABLE={
"80.99.244.113":"96-D0-CF-E2-03-BB",
"43.130.216.28":"98-D0-CF-E2-03-AE",
"170.114.52.85":"94-D0-CF-E2-03-TE",
"24.53.187.228":"98-D0-CF-E2-03-BQ",
"101.196.66.135":"93-D0-CF-E2-03-BW",
"251.206.106.90":"26-D0-CF-E2-03-BE",
"197.177.28.27":"86-D0-CF-E2-03-5E",
"29.34.136.94":"98-D0-CF-E2-03-BG",
"7.107.225.203":"26-D0-CF-E2-03-WE",
"69.98.22.46":"66-D0-CF-E2-03-EE"}
s.bind(('',12345))
s.listen(5)
while True:
    c,adr=s.accept()
    print("Address Resolution Protocol")
    print("connceted to ",adr)
    inp=c.recv(1024).decode()
    out=(ARP_TABLE[inp])
    c.send(out.encode())
    c.close()
    print("Connection Closed",adr)

    
import socket
s= socket.socket()
ARP_TABLE={
"96-D0-CF-E2-03-BB":"80.99.244.113",
"98-D0-CF-E2-03-AE":"43.130.216.28",
"94-D0-CF-E2-03-TE":"170.114.52.85",
"98-D0-CF-E2-03-BQ":"24.53.187.228",
"93-D0-CF-E2-03-BW":"101.196.66.135",
"26-D0-CF-E2-03-BE":"251.206.106.90",
"86-D0-CF-E2-03-5E":"197.177.28.27",
"98-D0-CF-E2-03-BG":"29.34.136.94",
"26-D0-CF-E2-03-WE":"7.107.225.203",
"66-D0-CF-E2-03-EE":"69.98.22.46",
}
s.bind(('',12345))
s.listen(5)
while True:
    c,adr=s.accept()
    print("Reverse Address Resolution Protocol")
    print("connceted to ",adr)
    inp=c.recv(1024).decode()
    out=(ARP_TABLE[inp])
    c.send(out.encode())
    c.close()
    print("Connection Closed",adr)

    
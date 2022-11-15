import os
site=input("Enter the IP Address/ Domain Name you want to traceroute:")
print(os.popen("tracert " + site).read())
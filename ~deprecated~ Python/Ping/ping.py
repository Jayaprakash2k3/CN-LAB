import os
site=input("Enter the IP Address/ Domain Name you want to ping:")
print(os.popen("ping " + site).read())
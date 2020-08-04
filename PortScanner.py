#!/bin/python3
#Tool for Scanning Open port in a Network
#Written by Abhijith A
#Date: 04-08-2020

import sys,socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Wrong number of arguments provided")
    print("Syntax: python3 portscanner.py <ipv4 address>")
    sys.exit()

print("-"*100)
print("Scanning started at "+ str(datetime.now()))
print("Checking for Open ports from 1 - 65535")
print("-"*100)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(" Port {} is open ".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nProcess Interrupted")
    sys.exit()

except socket.error:
    print("\nConnection Problem with Server")
    print("Check the Connectiona and try again...")
    sys.exit()

except socket.gaierror:
    print("\nHostname couldn't be resolved")
    sys.exit()
    
print("-"*100)
print("Scan Completed at "+ str(datetime.now()))
print("-"*100)
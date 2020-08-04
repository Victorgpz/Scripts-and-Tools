#!/bin/python3
#Tool for Scanning Open ports in a Network
#Written by Abhijith A
#Date: 04-08-2020
#Still a prototype


import sys,socket
import threading
import time
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Wrong number of arguments provided")
    print("Syntax: python3 portscanner.py <ipv4 address>")
    sys.exit()

print("-"*50)
print("Scanning started at "+ str(datetime.now()))
print("Checking for Open ports from 1 - 65535")
print("-"*50)
print("\n")


def scan(port):

     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     socket.setdefaulttimeout(1)
     result = s.connect_ex((target,port))
     if result == 0:
         print(" Port {} is open ".format(port))
     s.close()
     #print(time.perf_counter())

threads = []

try:
    for i in range(1,65535):
        t = threading.Thread(target=scan,args=[i])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nProcess Interrupted")
    sys.exit()

except socket.error:
    print("\nConnection Problem with Server")
    print("Check the Connections and try again...")
    sys.exit()

except socket.gaierror:
    print("\nHostname couldn't be resolved")
    sys.exit()

except:
    print("Threading Error")
    sys.exit()

print("\n")
print("-"*50)
print("Scan Completed in {} seconds ".format(round(time.perf_counter(),2)))
print("-"*50)
sys.exit()
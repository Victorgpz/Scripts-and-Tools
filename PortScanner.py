#!/bin/python3
#Tool for Scanning Open ports in a Network
#Written by Abhijith A
#Date: 04-08-2020
#Still a prototype

from queue import Queue
import sys,socket
import threading
import time
from datetime import datetime

queue = Queue()
open_ports = []

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
    try:
         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         s.connect((target,port))
         s.close()
         return True
    except:
        return False


threads = []
for port in range(65535):
    queue.put(port)

def run():
       try:
            while not queue.empty():
                port = queue.get()
                if scan(port):
                    print("Port {} is open!".format(port))
                    open_ports.append(port)
       except KeyboardInterrupt:
            print("\nProcess Interrupted")
            exit()

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


try:
    for i in range(100):
        t = threading.Thread(target=run)
        threads.append(t)
        t.daemon = True # die when main  thread die

    for t in threads:
        t.start()

    for thread in threads:
            thread.join()


except KeyboardInterrupt:
    print("\nProcess Interrupted")
    exit()

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
print("The open ports are ",open_ports)
print("Scan Completed in {} seconds ".format(round(time.perf_counter(),2)))
print("-"*50)
sys.exit()
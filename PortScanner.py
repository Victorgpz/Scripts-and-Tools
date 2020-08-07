#!/bin/python3
#Tool for Scanning Open ports in a Network
#Written by Abhijith A
#Date: 04-08-2020
#edited by @victorgpz
#Date: 07-08-2020
#Still a prototype

from queue import Queue
import sys,socket
import threading
import time
from datetime import datetime
import argparse
start=time.time()
ap=argparse.ArgumentParser();
ap.add_argument("-t","--host",required=True,
help="target ip adderss")
ap.add_argument("-p","--port",help="")
args=vars(ap.parse_args())


queue = Queue()
open_ports = []
op=[]

if not args["port"]:
    for i in range(65535):
     queue.put(i)
    op.append(1)
    op.append(65535)
else:
    op=args["port"].split("-")
    for i in range(int(op[0]),int(op[1])+1):
        queue.put(i)
target=args["host"]

print("-"*50)
print("Scanning started at "+ str(datetime.now()))
print("Checking for Open ports from {0} - {1}".format(int(op[0]),int(op[1])))
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
end=time.time()
print("\n")
print("-"*50)
print("The open ports are ",open_ports)
print("Scan Completed in {} seconds ".format(round(end-start,2)))
print("-"*50)
sys.exit()
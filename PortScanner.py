#!/bin/python3
#Tool for Scanning Open ports in a Network
#Written by Abhijith A
#Date: 04-08-2020
#edited by @victorgpz
#Still a prototype

import threading, socket, sys, time
from queue import Queue
from datetime import datetime
import argparse
start=time.time()
#Arguments Parsing
ap=argparse.ArgumentParser()
ap.add_argument("-t","--host",required=True , help="Target ip adderss or hostname ,eg: -t 127.0.0.1 ")
ap.add_argument("-p","--port",help="Target Port Range ,eg: -p 0-1000")
args=vars(ap.parse_args())


queue = Queue()
open_ports = []
op=[]

try:
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

except:
    print("Wrong Syntax")
    print("Syntax: python PortScanner.py -t <ip> -p <port_range>")
    print("Example: python PortScanner.py -t 127.0.0.1 -p 0-1000")
    sys.exit()

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            print('Port: ' + str(port) + ' is open')
            open_ports.append(port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

threads = []

for x in range(thread):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

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
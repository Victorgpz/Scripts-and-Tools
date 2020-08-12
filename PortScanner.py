#!/bin/python3
#Tool for Scanning Open ports in a Network
#Written by Abhijith A
#Date: 04-08-2020
#edited by @victorgpz
#Date: 12-08-2020
#Still a prototype

import threading, socket, sys, time
from queue import Queue
from datetime import datetime
import argparse

print_lock = threading.Lock()

start=time.time()

ap=argparse.ArgumentParser();
ap.add_argument("-t","--host",required=True,
help="target ip adderss")
ap.add_argument("-p","--port",help="port range")
ap.add_argument("-z","--thread",help="no of threads")
args=vars(ap.parse_args())

open_ports = []
op=[]

host = args["host"]

if not args["thread"]:
    thread=100
else:
    thread=int(args["thread"])

if not args["port"]:
    op.append(1)
    op.append(65535)
else:
    op=args["port"].split("-")

print("-"*50)
print("Scanning started at "+ str(datetime.now()))
print("Checking for Open ports from {0} - {1}".format(int(op[0]),int(op[1])))
print("-"*50)
print("\n")


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

q = Queue()

for x in range(thread):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(int(op[0]),int(op[1])):
    q.put(worker)
end=time.time()
print("\n")
print("-"*50)
print("The open ports are ",open_ports)
print("Scan Completed in {} seconds ".format(round(end-start,2)))
print("-"*50)
sys.exit
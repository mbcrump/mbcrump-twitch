#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DDoS application for fun and play
   Twitch 
   Port 8080 only
"""
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket.bind(('localhost', 8080))

serversocket.listen(5)  # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    print(buf)

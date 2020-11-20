#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DDoS application for fun and play
   Twitch 
   Port 8080 only
"""
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8080))
clientsocket.send('hello')
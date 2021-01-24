
# Notes
# Host	irc.root-me.org
# Protocol	IRC
# Port	6667
# IRC channel	#root-me_challenge
# Bot	candy

import socket
import sys
import math

server = "irc.root-me.org"       #settings
channel = "#root-me_challenge"
botnick = "rainbowren10"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket
print("connecting to:" + server)
irc.connect((server, 6667))  # connects to the server

irc.send(("JOIN " + channel + "\n").encode())
irc.send(
    ("USER rr irc.root-me.org root-me :Candy" + "\n").encode()
)  # user authentication
irc.send(("PRIVMSG nickserv :!ep1\r\n").encode())
irc.send(("NICK " + botnick + "\n").encode())

while True:
    text = irc.recv(2020).decode()
    print(text)  # print text to console
    irc.send('PRIVMSG ' + channel + ' :!ep1 \r\n')
    if text.find('/') != -1:    
      squareroot = math.sqrt(text.split() [1])
      answer = squareroot * text.split() [2]
      print("FULL" + text)
      print("SR" + squareroot)
      print("AN" + answer)
      #irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
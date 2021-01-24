
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
botnick = "gamesys3"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print ("connecting to: "+ server)
irc.connect((server, 6667))                                                         #connects to the server
irc.send(("NICK " + botnick + "\n").encode()) # sets nick#user authentication
#irc.send(("PRIVMSG nickserv :iNOOPE\r\n").encode())    #auth
irc.send(("JOIN "+ channel +"\n").encode())        #join the chan

while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print (text)   #print text to console

   if text.find('/') != -1:    
      squareroot = math.sqrt(text.split() [1])
      answer = squareroot * text.split() [2]
      print("FULL" + text.decode())
      print("SR" + squareroot)
      print("AN" + answer)
      #irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)

#! /usr/bin/python3
# Notes
# Host	irc.root-me.org
# Protocol	IRC
# Port	6667
# IRC channel	#root-me_challenge
# Bot	candy

import socket
import sys
import math

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.root-me.org"  # settings
channel = "#root-me_challenge"
nick = "rainbowren10"
botname = "Candy"


def joinchan(chan):  # join channel(s).
    ircsock.send(bytes("JOIN " + chan + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)


def sendmsg(msg, target=channel):  # sends messages to the target.
    ircsock.send(bytes("PRIVMSG " + target + " :" + msg + "\n", "UTF-8"))


def joinserv(server):
    # Here we connect to the server using the port 6667
    ircsock.connect((server, 6667))
    # We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
    ircsock.send(bytes("USER " + nick + " " + nick +
                       " " + nick + " " + nick + "\n", "UTF-8"))
    # assign the nick to the bot
    ircsock.send(bytes("NICK " + nick + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find('MODE rainbowren10') == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def main():
    joinserv(server)
    joinchan(channel)
    sendmsg('!ep1', botname)
    while True:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip("\r\n")
        print(ircmsg)  # print text to console
        if ircmsg.find('PRIVMSG') != -1:
            print(ircmsg)
            # sample message -
            # :Candy!Candy@root-me.org PRIVMSG rainbowren10 :399 / 6768
            msg1 = ircmsg.split(" ")
            print(msg1[3][1:])
            print(msg1[5])
            squareroot = math.sqrt(int(msg1[3][1:]))
            answer = round(squareroot * int(msg1[5]), 2)
            print(squareroot)
            print(answer)
            sendmsg("!ep1 -rep " + str(answer), botname)
main()

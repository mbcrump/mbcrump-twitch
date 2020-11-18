#!/usr/bin/env python3
## be able to quickly find password using alpha characters
## no password file
## build engine to do it ourselves
import random
import time 

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
chars_list = list(chars)
password = input("What is your pw?") ##kiradeveloper

guess_password = ""

i = 0
named_tuple = time.localtime()
seconds = time.time()
print("Starting time" + time.strftime("%m/%d/%Y, %H:%M:%S:" + str(seconds), named_tuple))
while (guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    #print("App tried" + str(guess_password))
    i += 1
    if (guess_password == list(password)):
        print("Your password is = " + "".join(guess_password))
        print("Total number of guesses = " + str(i))
        named_tuple = time.localtime()
        seconds = time.time()
        print("Stop time" + time.strftime("%m/%d/%Y, %H:%M:%S:" + str(seconds), named_tuple))
        break

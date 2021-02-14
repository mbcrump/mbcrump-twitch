#!/usr/bin/python3
"""Brute-forces a ROT cipher
http://cmattoon.com/infosec-institute-ctf-level-4/
"""


def rot(text, n):
    """Rotates 'text' by 'n' positions"""
    output = ''
    for char in text.lower():  # don't use uppercase values
        x = ord(char)
        if (x >= ord('a') and x <= ord('z')):
            x += n  # Rotate the character
            if (x > ord('z')):  # Wrap it around, if it extends past 'z'
                x = (ord('a')-1) + (x - ord('z'))
            output += chr(x)
        else:
            # It's not a letter
            output += char
    return output


ciphertext = 'Aipgsqi fego, xlmw pizip mw rsx ew iewc ew xli pewx fyx wxmpp rsx xss gleppirkmrk. Ws ks elieh erh irxiv xlmw teww: wlmjxxlexpixxiv'

for i in range(0, 26):
    pt = rot(ciphertext, i)
    if 'infosec' in pt or 'flag' in pt:
        print("\033[91mKey: %d, Plaintext: %s\033[0m" % (i, pt))
    else:
        print("Key: %d, Plaintext: %s" % (i, pt))

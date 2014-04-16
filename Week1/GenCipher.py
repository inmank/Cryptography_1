'''
Created on Apr 16, 2014

@author: karthik
'''

import sys
from random import random

MSGS = ("---  11 secret messages  ---")
   
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def getRandom(size=16):
    return 

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = getRandom(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

if __name__ == "__main__":
    main()
    
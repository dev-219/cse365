import argparse
import os
import time
#import socket
import sys
import string
#from aes import AESCipher
#from Crypto.PublicKey import RSA

# MESSEGE = 'AXEEH'
MESSEGE = 'FLYZHUVKFULAOYLLZSVHKLKWSHBKPAZKLJWYVWOLZFPUNNSHBJVTHZZALUJPSSPUNYLAVYALKAOVAOHYYVDZDOPTZLFWSHUALKWYLMPNBYLHWWSLZLLKZRHALZHJLZPTWBYPAPLZTPUPHABYPGLZJHSJBSHAVYZKPZWLYZPVUZZBWLYZAHYZMVYLZLLUDOPAASLZRULL'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(key, messege):
    plaintext = ''
    for i in range(len(messege)):
        newChar = ord(messege[i])-key
        if ( newChar < 65):
            newChar += 26
        elif ( newChar > 90):
            newChar -= 26
        plaintext+=chr(newChar)
    print(plaintext)

decrypt(7, MESSEGE)
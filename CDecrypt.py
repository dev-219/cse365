import argparse
import os
import time
#import socket
import sys
import string
#from aes import AESCipher
#from Crypto.PublicKey import RSA

# # Handle command-line arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("-c", "--cipher",
#                     help='cipher... caesar or julia',
#                     required=True)
# parser.add_argument("-d", "--decrypt",
#                     help='Decrypt a file',
#                     required=False)
# parser.add_argument("-e", "--encrypt",
#                     help='Encrypt a file',
#                     required=False)
# parser.add_argument("-o", "--outfile",
#                     help='Output file',
#                     required=False)

# args = parser.parse_args()
MESSEGE = 'OLSSV'
# MESSEGE = 'FLYZHUVKFULAOYLLZSVHKLKWSHBKPAZKLJWYVWOLZFPUNNSHBJVTHZZALUJPSSPUNYLAVYALKAOVAOHYYVDZDOPTZLFWSHUALKWYLMPNBYLHWWSLZLLKZRHALZHJLZPTWBYPAPLZTPUPHABYPGLZJHSJBSHAVYZKPZWLYZPVUZZBWLYZAHYZMVYLZLLUDOPAASLZRULL'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(key, messege):
    plaintext = ''
    for i in range(len(messege)):
        if ((ord(messege[i])-key >= 65 and ord(messege[i])-key <= 90)):
            plaintext+=chr(ord(messege[i])-key)
        else:
            plaintext += ' '
    print(plaintext)
    
decrypt(7,MESSEGE)
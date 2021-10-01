import argparse
import os
import time
#import socket
import sys
import string
#from aes import AESCipher
#from Crypto.PublicKey import RSA

plaintext = 'Hello'

def lrot(n, d): 
    return ((n << d)|(n >> (8 - d)))&0xff

keybytes = bytes(os.urandom(13))

print(keybytes)

keyshift = keybytes[0] % 7 + 1

print(keybytes)

keyxor = [] 
keyxorasstring = ""
for i in range(1, 13):
    keyxor.append(ord(string.ascii_letters[keybytes[i] % len(string.ascii_letters)]))
    keyxorasstring = keyxorasstring + chr(keyxor[i-1])
# print('Key is shifting by ' + str(keyshift) + ' and XORing with ' + keyxorasstring)
ciphertext = []
for i in range(0, len(plaintext)):
    ciphertext.append(lrot(plaintext[i], keyshift) ^ keyxor[i % len(keyxor)])

print(bytes(ciphertext))

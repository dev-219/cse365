import argparse
import os
import time
#import socket
import sys
import string
import gzip
#from aes import AESCipher
#from Crypto.PublicKey import RSA


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt",
                    help='Decrypt a file',
                    required=True)
parser.add_argument("-o", "--outfile",
                    help='Output file',
                    required=False)

args = parser.parse_args()


data = open(args.decrypt, "rb").read()

cyphertext = str(gzip.decompress(data))




def lrot(n, d): 
    return ((n << d)|(n >> (8 - d)))&0xff

keybytes = bytes(os.urandom(13))

print('keybytes: ')
print(keybytes)

keyshift = 5

print('keyshift: ') 
print(keyshift)

keyxor = [] 
keyxorasstring = ""
for i in range(1, 13):
    keyxor.append(ord(string.ascii_letters[keybytes[i] % len(string.ascii_letters)]))
    keyxorasstring = 'CBgMbeHMhfeu'
print('Key is shifting by ' + str(keyshift) + ' and XORing with ' + keyxorasstring)
plaintext = []
for i in range(0, len(cyphertext)):
    plaintext.append(lrot(cyphertext[i], keyshift) ^ keyxor[i % len(keyxor)])

print(plaintext)

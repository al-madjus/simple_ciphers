#!/usr/bin/python
# Takes a string and shift encrypts or decrypts it using the 
# supplied rotation
import argparse

# Add arguments
parser = argparse.ArgumentParser(description="Encrypt/decrypt Caesar cyphers")
parser.add_argument("mode", help="Encrypt or decrypt", nargs="?", choices=("encrypt", "decrypt"))
parser.add_argument("string", help="String to encrypt/decrypt")
parser.add_argument("rot", help="Rotation to use")
args = parser.parse_args()

# Definitions
mode = args.mode
string = args.string.lower()
rot = int(args.rot)

def encrypt(string, rot):
    """Caesar encryption function"""
    cypherstr = ""
    for char in string:
        if not char.isalpha():
            cypher = char
        elif char.isalpha():
            num = ord(char)
            cypher = (num - 97 + rot) % 26
            cypher = chr(cypher + 97)
        cypherstr += cypher
    return cypherstr

def decrypt(string, rot):
    """Caesar decryption function"""
    plainstr = ""
    for char in string:
        if not char.isalpha():
            plain = char
        elif char.isalpha():
            num = ord(char)
            plain = (num - 97 - rot) % 26
            plain = chr(plain + 97)
        plainstr += plain
    return plainstr

# Either encrypt or decrypt
if mode == "encrypt":
    print(encrypt(string, rot))
elif mode == "decrypt":
    print(decrypt(string, rot))

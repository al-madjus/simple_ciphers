#!/usr/bin/python
# Takes a string and encrypts or decrypts using the affine cypher
import argparse

# Add arguments
parser = argparse.ArgumentParser(description="Encrypt/decrypt affine cyphers")
parser.add_argument("mode", help="Encrypt or decrypt", nargs="?", choices=("encrypt", "decrypt"))
parser.add_argument("string", help="String to encrypt/decrypt")
parser.add_argument("a", help="Value for a")
parser.add_argument("b", help="Value for b")
args = parser.parse_args()

# Definitions
mode = args.mode
string = args.string.lower()
a = int(args.a)
b = int(args.b)

def encrypt(string, a, b):
    """Affine encryption function"""
    cypherstr = ""
    for char in string:
        if not char.isalpha():
            cypher = char
        elif char.isalpha():
            num = ord(char) - 97
            cypher = (a * num + b) % 26
            cypher = chr(cypher + 97)
        cypherstr += cypher
    return cypherstr

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
    
def findinverse(a):
	"""Finds modular inverse of a"""
	g, x, y = egcd(a, 26)
	if g != 1:
		raise Exception("Modular inverse of a does not exist")
	else:
		return x % 26
   
def decrypt(string, a, b):
    """Affine decryption function"""
    plainstr = ""
    ainv = findinverse(a)
    print(ainv)
    for char in string:
        if not char.isalpha():
            plain = char
        elif char.isalpha():
            num = ord(char) - 97
            plain = (ainv * (num - b)) % 26
            plain = chr(plain + 97)
        plainstr += plain
    return plainstr	

# Either encrypt or decrypt
if mode == "encrypt":
    print(encrypt(string, a, b))
elif mode == "decrypt":
	print(decrypt(string, a, b))

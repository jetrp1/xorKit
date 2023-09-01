#!/usr/bin/env python3

# Built by Ryan Peel
# A large Majority of this code is based on the Shift.py pregram provided by Dr. Harrison at UTSA

# Built for use in breaking XOR encryption

from argparse import ArgumentParser, FileType
from sys import stdin, stdout
from time import sleep

parser = ArgumentParser(description='A Program to count Coincidences in an encrypted file', prog='Coincidences.py')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('shift', type=int)
parser.add_argument('infile', nargs='?', type=FileType('rb'), default=stdin)
args = parser.parse_args()

# A simple function to check for null bytes
# Implemented for readability
def is_Null_Byte(inByte: bytes):
    if inByte == b'\x00':
        return True
    
    return False

byteList = args.infile.read()
C_Count = 0

for i in range(len(byteList)):
    if byteList[i] == byteList[(i + args.shift) % len(byteList)]:
        C_Count += 1

# I thought i could shift then xor and count the null bytes, but that did not work
    '''
    xored = byteList[i] ^ byteList[(i + args.shift) % len(byteList)] 

    print(xored, is_Null_Byte(xored))
    sleep(.5)

    if is_Null_Byte(xored):
        C_Count += 1

        '''

if args.verbose:
    print("Shift: %d \tCoincidences: %d" % (args.shift, C_Count))
else:
    print(C_Count)

exit()
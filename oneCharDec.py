#!/usr/bin/env python3

# Built by Ryan Peel


from argparse import ArgumentParser, FileType
from sys import stdin, stdout

parser = ArgumentParser(description='attempts to decrypt a single byte of a key', prog='OneCharDec.py')
parser.add_argument('-v', '--verbose', action='store_true') # Prints the entire outfile, instead of just the bytes which were xored
parser.add_argument('shift', type=int) # Essentially the length of the key
parser.add_argument('offset', type=int) # Position in the key
parser.add_argument('key', type = str) # Single character Key
parser.add_argument('infile', nargs='?', type=FileType('rb'), default=stdin)
parser.add_argument('outfile', nargs='?', type=FileType('wb'), default=stdout)
args = parser.parse_args()

inbytes = args.infile.read()
key = args.key.encode()
outbytes = []
toXOR = []

# Bytes to xor
for i in range(args.offset, len(inbytes), args.shift):
    toXOR.append(i)

if args.verbose:
    print("Size of input recieved: %d" % len(inbytes))
    print("Number of bytes to XOR: %d" % len(toXOR))


if args.verbose:
    for i in range(len(inbytes)): 
        print("i = %d" % i)
        if i in toXOR: # Byte to be XORed
            outbytes.append(inbytes[i] ^ key[0])
        else: 
            outbytes.append(inbytes[i])
else:
    for i in toXOR: # Only the bytes we want to XOR
        outbytes.append(inbytes[i] ^ key[0])
    
args.outfile.write(bytes(outbytes))
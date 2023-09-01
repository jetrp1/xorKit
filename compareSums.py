#!/usr/bin/env python3

# Built By Ryan Peel to compare a large set os sha256 sums against one sum (key)
# this was a one off script used to workaround a bug in xor-analyze where the probable key given was one byte off.
# Another simple one liner bash script was used to decrypt using all alphanumberic options for that one bit in the key.
# Afer this i compared the sha256 sums of each of these to the expected sum and then found the correct key  

from argparse import ArgumentParser, FileType
from sys import stdin, stdout
import hashlib

parser = ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('key')
# parser.add_argument('infile', nargs='?', type=FileType('r'), default=stdin)
args = parser.parse_args()

line = stdin.readline().strip()


while line:
    # create sha256 sum
    f = open(line, 'rb')
    data = f.read()
    currSum = hashlib.sha256(data).hexdigest();
    isCorrectKey = (currSum == args.key)

    if args.verbose:
        print("{0}: {1}".format(line, str(isCorrectKey)))
    else:
        if isCorrectKey:
            print("{0}: {1}".format(line, str(isCorrectKey)))
    
    line = stdin.readline().strip()
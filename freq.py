#!/bin/env python3

# Built by Ryan Peel

from argparse import ArgumentParser
import sys

parser = ArgumentParser("Builds a frequency Table and write table to sdtout")
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

# Get input files from sdtin
inputFiles = []
line = sys.stdin.readline()

while line:
    inputFiles.append(line.strip())
    line = sys.stdin.readline()

totalCount = 0
countList = []

for i in range(256):
    countList.append(0)

for item in inputFiles:
    currFile = open(item, 'rb')
    currByte = currFile.read(1)
    
    while currByte:
        countList[int.from_bytes(currByte, 'little')] += 1
        totalCount += 1
        currByte = currFile.read(1)
    
    currFile.close()

mostFreq = 0

for i in range(len(countList)):
    currFreq = countList[i] / totalCount
    if args.verbose:
        print("%d %10.10f" % (i, currFreq))
        if countList[mostFreq] < countList[i]:
            mostFreq = i
    else:
        print("%10.10f" % currFreq)

if args.verbose:
    print("\n %d is the most common byte" % mostFreq)

exit()
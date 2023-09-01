#!/bin/env python3

import os
import sys

data = []

for line in sys.stdin:
    data.append(line)

if len(data) != 256:
    print("Input Length incorrect")

mostFreq = 0

for i in range(len(data)):
    if data[mostFreq] < data[i]:
        mostFreq = i

    string = str(i) + " " + chr(i) + " " + str(float(data[i]))
    print(string)

print("\n", "Most Frequent is " + str(mostFreq) + " ( " + chr(mostFreq) + " ) with " + str(float(data[mostFreq])) + "%\n")
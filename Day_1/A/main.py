#!/bin/python
# Day 1 > A

freq = 0

file_input = open("./input", "r")

for i in file_input.read().split('\n'):
    try:
        freq += int(i)
    except:
        pass

file_input.close()
print(freq)
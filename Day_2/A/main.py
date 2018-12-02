#!/bin/python
# Day 2 > A

from string import ascii_lowercase

count = [0, 0] # [2's count, 3's count]

file_input = open("./input", "r")
IDs = file_input.read().lower().split('\n')

counts = [[i.count(j) for j in ascii_lowercase] for i in IDs]
counts = [[i.count(2), i.count(3)] for i in counts]

for i in counts:
    if(i[0] > 0):
        count[0] += 1
    if(i[1] > 0):
        count[1] += 1

file_input.close()
print(counts)
print(count)
print(count[0]*count[1])
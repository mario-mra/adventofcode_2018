#!/bin/python
# Day 2 > B

# Use itertools for permutations!!!

def diff(A, B):
    result = [0, []]
    for i,j in enumerate(A):
        try:
            if(j!=B[i]):
                result[0] += 1
                result[1].append(i)
        except:
            break
    return result

file_input = open("./input", "r")
IDs = file_input.read().lower().split('\n')
file_input.close()

diffs = []
for i,j in enumerate(IDs):
    for k,m in enumerate(IDs[i+1:]):
        diffs.append([i, k+i+1]+diff(j, m))

for i in diffs:
    if(i[2] == 1):
        result = i
        break

print(result)

items = result[0:2]
pos = result[-1][0]
print("{:3} - {}".format(items[0], IDs[items[0]]))
print("{:3} - {}".format(items[1], IDs[items[1]]))
print("{}^".format((6+pos)*' '))

print("{}{}".format(IDs[items[1]][:pos], IDs[items[1]][pos+1:]))
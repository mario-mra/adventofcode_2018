#!/bin/python
# Day 3 > A & B

# .---->
# |    x
# |
# v y
# Offset => [x, y]
# Size   => [x, y]

class claim:
    def __init__(self, claim):
        c = claim.replace(' ', '').split('@')
        self.id = int(c[0][1:])
        data = c[1].split(':')
        self.offset = [int(i) for i in data[0].split(',')]
        self.size   = [int(i) for i in data[1].split('x')]
        self.overlap = False

class fabric:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.fabric = [[[0, []] for j in range(width)] for i in range(height)]

    def print_fabric(self):
        for r in self.fabric:
            [print(self.pr_symbol(c[0]), end='') for c in r]
            print()

    def add_claims(self, claims):
        for claim in claims:
            offset = claim.offset
            size = claim.size
            c_id = claim.id
            for r in range(offset[1], offset[1]+size[1]):
                for c in range(offset[0], offset[0]+size[0]):
                    fbr = self.fabric[r][c]
                    fbr[0] += 1
                    fbr[1].append(c_id)
                    if(len(fbr[1])>1):
                        for cl in fbr[1]:
                            claims[cl-1].overlap = True

    def pr_symbol(self, num):
        if(num==0):
            return '.'
        elif(num==1):
            return '#'
        else:
            return 'x'

    def count_overlaps(self):
        overlaps = 0
        for i in self.fabric:
            for j in i:
                if(j[0]>1):
                    overlaps += 1
        return overlaps


def parse_claims(claims):
    p_claims = []
    for c in claims:
        try:
            p_claims.append(claim(c))
        except:
            pass
    return p_claims


input_file = open("input", 'r')
claims = input_file.read().split('\n')
input_file.close()

p_claims = parse_claims(claims)

fa = fabric(1000, 1000)
fa.add_claims(p_claims)

for i in p_claims:
    if(i.overlap == False):
        print("Claim that doesn't overlap: {}. At: {}".format(i.id, i.offset))

fa.print_fabric()
# print(fa.count_overlaps())
# print(fa.fabric)
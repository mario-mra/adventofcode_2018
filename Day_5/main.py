#!/bin/python

# Day 5 A&B

from string import ascii_lowercase as al
from string import ascii_uppercase as au

def react_polymer(polymer):
    done = False
    c_done = 0
    while(not(done)):
        done = True
        for i,j in enumerate(polymer[1:][::-1]):
            prev = polymer[-1*(i+2)]
            if(i >= c_done):
                if((j.islower() and prev == au[al.index(j)]) or \
                (j.isupper() and prev == al[au.index(j)])):
                    polymer = polymer[:-1*(i+2)] + polymer[-i:]
                    done = False
                    c_done = i-1
                    break
            else:
                pass
    return polymer

if(__name__ == "__main__"):
    # Part A
    print("## Part A ##")
    input_file = open('input', 'r')
    polymer = input_file.read().strip()
    pol_len_pre = len(polymer)
    # print("Input polymer => {}".format(polymer))
    input_file.close()

    polymer = react_polymer(polymer)

    # print("Output polymer => {}".format(polymer))
    print("Original polymer length: {}\nNew polymer length: {}".format(pol_len_pre, len(polymer)), end="\n\n")
    
    
    # Part B
    print("## Part B ##")
    pol_len_pre = len(polymer)

    tests = []
    for i in al:
        units = [i, i.upper()]
        print("Testing polymer reaction without units {}/{} ... ".format(units[0], units[1]), end='')
        polymer_test = polymer.replace(units[0], '')
        polymer_test = polymer_test.replace(units[1], '')
        polymer_test_len = len(react_polymer(polymer_test))
        print("Lenght of the new polymer: {} units \n".format(polymer_test_len))
        tests.append([polymer_test_len, units])
        del polymer_test

    best_test = min(tests, key=lambda x: x[0])
    print()
    print("Best polymer reaction removing the units {}/{} obtaining a length of {}".format(best_test[1][0], best_test[1][1], best_test[0]))
#!/bin/python
# Day 1 > A

freq = []
rep = 0

file_input = open("./input", "r")
freqs_list = file_input.read().split('\n')

num_iter = 0
found = False
while(not(found)):
    if(num_iter == 0):
        freq.append([0])
    else:
        freq.append([freq[-1][-1]])
    
    for i in freqs_list:
        try:
            new_freq = freq[num_iter][-1]+int(i)
            if(num_iter != 0):
                if(new_freq in freq[0]):
                    rep = new_freq
                    found = True
                    break
            freq[num_iter].append(new_freq)
        except:
            pass

    num_iter += 1

file_input.close()
# print(freq)
print("Found freq {} at iteration {}.".format(rep, num_iter))
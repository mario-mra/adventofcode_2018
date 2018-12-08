#!/bin/python

# Day 8 A&B

from copy import deepcopy as dc
from time import time_ns

class node_obj:
    def __init__(self, u_entrie, add_id=0, verbose=False):
        self.id = add_id
        self.header = u_entrie[0:2]
        self.subnodes = parse_entries(u_entrie[2:], self.header[0], verbose=verbose)
        self.size = 2 + sum([i.size for i in self.subnodes]) + self.header[1]
        self.metadata = u_entrie[self.size-self.header[1]:self.size]

        # Part A: sum of all metadata
        self.sub_sum = sum(self.metadata)
        self.sub_sum += sum([i.sub_sum for i in self.subnodes])
        
        # Part A: nodes values
        if(len(self.subnodes) == 0):
            self.value = sum(self.metadata)
        else:
            child_value = []
            for i in self.metadata:
                if(i == 0):
                    continue
                if(len(self.subnodes) > (i-1)):
                    child_value.append(self.subnodes[i-1].value)
            self.value = sum(child_value)

        (print("Node with ID: {} has {} subnodes, a total length of {} and its metadata is {}." \
               .format(self.id, len(self.subnodes), self.size, self.metadata)) if verbose else None)

def parse_entries(entries, count, verbose=False):
    nodes = []
    
    for i in range(count):
        header = entries[0:2]
        if(len(header) == 0):
            break
        new_id = time_ns()
        (print("Creating node with ID: {} and header {}".format(new_id, header)) if verbose else None)
        nodes.append(node_obj(entries, add_id=new_id, verbose=verbose))
        node_len = nodes[-1].size
        entries = entries[node_len:]

    return nodes

if __name__ == "__main__":
    # input_file = open('./input_test', 'r')
    input_file = open('./input', 'r')
    entries = [int(i) for i in input_file.readline().split(' ')]
    input_file.close()

    node = node_obj(dc(entries), add_id='root', verbose=False)

    print("Part A")
    print("Sum of all metadata entries = {}\n".format(node.sub_sum))

    print("Part B")
    print("Value of the root node = {}".format(node.value))

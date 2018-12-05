#!/bin/python

import main
import matplotlib.pyplot as plt

size = [1000, 1000]

if __name__ == "__main__":
    claims = main.input_process()
    fabric = main.fabric_process(claims)

    plt.figure(1, figsize=(8, 8))
    plt.axis([0, size[0], 0, size[1]], 'equal', on=False)
    plt.gca().invert_yaxis()
    # plt.ylim(plt.ylim()[::-1])
    # plt.grid(True)
    plt.box(on=False)

    for i in claims:
        if(i.overlap):
            color = '#ffa206'
        else:
            color = '#00d821'
        off = i.offset
        size = i.size
        plt.fill([off[0], off[0]+size[0], off[0]+size[0], off[0]], [off[1], off[1], off[1]+size[1], off[1]+size[1]], color, edgecolor='b')
            
    plt.show()
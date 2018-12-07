#!/bin/python

# Day 6 A&B

import matplotlib.pyplot as plt
import random
r = lambda: random.randint(0,255)

class coordinate:
    def __init__(self, coor):
        self.x_pos = coor[0]
        self.y_pos = coor[1]
        self.pos = coor
        self.inf = False
        self.area = 0
        self.color = '#{:02X}{:02X}{:02X}'.format(r(), r(), r())
        self.dists = []
        self.ext_dists = [0, 0]

class coordinates:
    def __init__(self, coords=[], plt_en=False, plt_grid=False, plt_area=False, max_dist=10000):
        self.limits = None
        self.coordinates = []
        self.max_dist = max_dist
        self.size_max_dist = 0
        self.plt_en = plt_en
        self.plt_grid = plt_grid
        self.plt_area = plt_area
        self._plot_init_()
        if(coords!=[]):
            [self.add_coordinate(i) for i in coords]

    def _plot_init_(self):
        if(self.plt_en):
            self.fig = plt.figure(1, figsize=(8, 8))
            self.ax = self.fig.gca()

    def add_coordinate(self, coor):
        self.coordinates.append(coordinate(coor))

    def gen_limits(self, over=0.1):
        coords = self.coordinates

        coord_x = sorted([i.pos[0] for i in coords])
        diff_x = coord_x[-1]-coord_x[0]
        coord_y = sorted([i.pos[1] for i in coords])
        diff_y = coord_y[-1]-coord_y[0]

        self.limits = [[int(coord_x[0]-diff_x*over-1), int(coord_x[-1]+diff_x*over+1)], \
                       [int(coord_y[0]-diff_y*over-1), int(coord_y[-1]+diff_y*over+1)]]
        return self.limits

    def fill_area(self):
        limits = self.limits
        coords = self.coordinates

        if(self.plt_en):
            self.ax.set_xticks([i for i in range(limits[0][0], limits[0][1]+1, 1)])
            self.ax.set_yticks([i for i in range(limits[1][0], limits[1][1]+1, 1)])
            plt.axis(limits[0]+limits[1], 'equal')
            self.ax.invert_yaxis()
            plt.grid(visible=self.plt_grid)
        
        print("Filling row... ", flush=True, end='')
        for i in range(limits[0][0], limits[0][1]+1):
            print("#{}".format(i), flush=True, end=' ')
            for j in range(limits[1][0], limits[1][1]+1):
                dists = sorted([[self.tx_distance([i, j], c.pos), c] for c in coords], key=lambda x: x[0])
                
                if(sum([i[0] for i in dists]) < 10000):
                    self.size_max_dist += 1
                color = dists[0][1].color
                if(dists[0][0] == dists[1][0]):
                    if(self.plt_en):
                        plt.fill([i+0.5, i+0.5, i-0.5, i-0.5], [j-0.5, j+0.5, j+0.5, j-0.5], '#ffffff', edgecolor='b')
                        plt.plot(i, j, 'kx')
                else:
                    if(self.plt_en):
                        if(self.plt_area):
                            plt.fill([i+0.5, i+0.5, i-0.5, i-0.5], [j-0.5, j+0.5, j+0.5, j-0.5], color)
                        if(dists[0][0] == 0):
                            plt.plot(i, j, 'ko')
                    dists[0][1].area += 1
                    dists[0][1].dists.append(dists[0][0])
                    dists[0][1].ext_dists.append(sum([i[0] for i in dists]))
                    if(i in limits[0] or j in limits[1]):
                        dists[0][1].inf = True
        
        if(self.plt_en):
            plt.show()

    def larger_area(self):
        coords = []
        for i in self.coordinates:
            if(i.inf == False):
                coords.append([i.pos, i.area])
        return sorted(coords, key=lambda x: x[1])[-1]

    def tx_distance(self, p, q):
        return sum([abs(p[i]-q[i]) for i in range(len(p))])

    def print_coordinates(self):
        print([c.pos for c in self.coordinates])


if __name__ == "__main__":
    input_file = open("input_test", 'r')
    input_file = open("input", 'r')
    coordinates_l = [i.split(',') for i in input_file.read().replace(' ', '').split('\n')]
    coordinates_l = [[int(i[0]), int(i[1])] for i in coordinates_l]
    input_file.close()

    coords = coordinates(coordinates_l, plt_en=False, plt_grid=False, plt_area=False, max_dist=10000)

    print("Generating area limits... ", end='', flush=True)
    coords.gen_limits()
    print("Limits = {}".format(coords.limits), flush=True)

    print("Filling area... ", flush=True)
    coords.fill_area()
    print("Filling done!", flush=True)

    result_A = coords.larger_area()
    print("\nSolution A:")
    print("Larger area (not inf.) => coordinate {} with a total size of {}\n".format(result_A[0], result_A[1]))

    result_B = coords.size_max_dist
    print("Solution B:")
    print("Size of the region = {}".format(result_B))
#!/bin/python

# Day 6 A&B

class coordinate:
    def __init__(self, coor):
        self.x_pos = coor[0]
        self.y_pos = coor[1]
        self.pos = coor
        self.inf = False
        self.area = 0
        self.dists = []
        self.ext_dists = [0, 0]

class coordinates:
    def __init__(self, coords=[], max_dist=10000):
        self.limits = None
        self.coordinates = []
        self.max_dist = max_dist
        self.size_max_dist = 0
        if(coords!=[]):
            [self.add_coordinate(i) for i in coords]

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
        
        print("Filling row... ", flush=True, end='')
        for i in range(limits[0][0], limits[0][1]+1):
            print("#{}".format(i), flush=True, end=' ')
            for j in range(limits[1][0], limits[1][1]+1):
                dists = sorted([[self.tx_distance([i, j], c.pos), c] for c in coords], key=lambda x: x[0])
                
                if(sum([i[0] for i in dists]) < 10000):
                    self.size_max_dist += 1
                if(dists[0][0] != dists[1][0]):
                    dists[0][1].area += 1
                    if(i in limits[0] or j in limits[1]):
                        dists[0][1].inf = True

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

    coords = coordinates(coordinates_l, max_dist=10000)

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
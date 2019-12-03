# Problem description @ https://adventofcode.com/2019/day/3

"""

    There are smarter solutions compared to simulation:
    
        O(N^2): Check all pairs of line segments for intersection, going into the realm of computational geometry :c
        
        O(N log N) should be possible by processing line segments from left to right,
        however at that point this is completely overkill for an input where N = 301.
    
    As of right now the simulation solution takes ~150ms in Python2.7 and ~72ms in PyPy2, which is good enough in my book

"""


from time import time

lines = open("input.txt", "r").read().split()

""" 
Input parsing
"""

wire1 = []
wire2 = []
for line in lines[0].split(","):
    wire1.append((line[0], int(line[1:])))
for line in lines[1].split(","):
    wire2.append((line[0], int(line[1:])))

def simulate(grid, wire, is_first_wire = False):
    x = y = 0
    dist = dist1 = 1e18
    steps = 0
    for direction, length in wire:
        dx, dy = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0)
        }[direction]
        for move in xrange(length): # Process every point one-by-one
            steps += 1
            x += dx
            y += dy
            if (x, y) in grid:
                dist  = min(dist,  abs(x) + abs(y))
                dist1 = min(dist1, grid[x, y] + steps)
            elif is_first_wire:
                grid[x, y] = steps
    return dist, dist1

def solve(wireA, wireB):
    grid = {}
    simulate(grid, wireA, True)
    return simulate(grid, wireB)

t0 = time()

p1, p2 = solve(a1, b1)
print("Answer: %d for part 1, %d for part 2" % (p1, p2))
print("Time taken: %dms" % (1000 * (time() - t0)))

# Problem description @ https://adventofcode.com/2019/day/1

"""
Input parsing
"""

lines = open("input.txt", "r").readlines()
input_arr = map(int, lines)

def solve(input_arr):

    total = total2 = 0

    for fuel in input_arr:

        total += fuel // 3 - 2

        while fuel // 3 > 2:
            total2 += fuel // 3 - 2
            fuel = fuel // 3 - 2

    return total, total2

p1, p2 = solve(input_arr)
print "Answer: %d for part 1, %d for part 2" % (p1, p2)

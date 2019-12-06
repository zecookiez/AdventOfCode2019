# Problem description @ https://adventofcode.com/2019/day/2

"""
Input parsing
"""

lines = open("input.txt", "r").read().split(",")

input_arr = map(int, lines)

def calculate(arr, noun, verb):

    arr[1] = noun
    arr[2] = verb
    
    for p in xrange(0, len(arr), 4):
        if arr[p] == 1:
            arr[arr[p + 3]] = arr[arr[p + 1]] + arr[arr[p + 2]]
        elif arr[p] == 2:
            arr[arr[p + 3]] = arr[arr[p + 1]] * arr[arr[p + 2]]
        else:
            break
    
    return arr[0]

def solve(arr):

    for noun in xrange(100):
        for verb in xrange(100):
            if calculate(arr[:], noun, verb) == 19690720:
                return calculate(arr[:], 12, 2), 100 * noun + verb

    raise Exception("Impossible case!")

p1, p2 = solve(input_arr)
print("Answer: %d for part 1, %d for part 2" % (p1, p2))

import numpy as np


inFile = "day01/input.txt"

def partOne(inFile: str) -> int:
    with open(inFile) as f:
        maxval = 0                                          # max sum of calories from elves
        currval = 0                                         # current count of calories from current elf
        for line in f.readlines():                          # go through each value in the input txt line by line
            if line == "\n":                                # if it's a blank line then check current count to max value
                if currval > maxval:                        # if larger, make it max value and reset current count
                    maxval = currval
                    currval = 0
                else:                                       # else just reset current count and continue to next elf
                    currval = 0

            else:                                           # if not blank space then continue counting
                currval += int(line)

    return maxval

print("Solution of part one: ", partOne(inFile))

def partTwo(inFile: str) -> int:                            # basically a more general approach to part one
    counts = []                                             # sum up individual elves' calories as before, but store all values
    with open(inFile) as f:                                 # in a list
        currval = 0
        for idx, val in enumerate(f.readlines()):
            if val == "\n":
                counts.append(currval)
                currval = 0
            else:
                currval += int(val)

    return np.sum(sorted(counts)[::-1][:3])                 # sort the list and return sum of the three largest values

print("Solution of part two: ", partTwo(inFile))
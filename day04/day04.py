import numpy as np
import re


inFile = 'day04/input.txt'

def partOne(inFile: str) -> int:
    with open(inFile) as f:
        count = 0
        for line in f:
            vals = re.split(',|-', line.strip('\n'))                                # spliting the input line into list of strings of the numbers
            vals = list(map(int, vals))                                             # converting the strings to integers
            if  sorted(vals)[1:-1] == vals[2:] or sorted(vals)[1:-1] == vals[:2]:
                count += 1

    return count

print('Solution of part one: ', partOne(inFile))

def partTwo(inFile: str) -> int:
    with open(inFile) as f:
        count = 0
        for line in f:
            vals = re.split(',|-', line.strip('\n'))                                # splitting the data same as before
            vals = list(map(int, vals))
            if (min(vals[1], vals[3]) - max(vals[0], vals[2])) >= 0:                # condition must be true to have overlap
                count += 1

    return count

print('Solution of part two: ', partTwo(inFile))




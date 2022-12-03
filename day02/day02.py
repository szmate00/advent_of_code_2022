import numpy as np


inFile = 'day02/input.txt'

def partOne(inFile: str) -> int:                            
    count = 0
    values = {                                                  # we store all the possible outcomes in a dict
        ('A', 'X'): 4,
        ('A', 'Y'): 8,
        ('A', 'Z'): 3,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 7,
        ('C', 'Y'): 2,
        ('C', 'Z'): 6
    }
    with open(inFile) as f:
        for line in f:
            count += values[(line[0], line[2])]                # then simply add the corresponding value to the count 
    return count

print('Solution of part one: ', partOne(inFile))

def partTwo(inFile: str) -> int:
    count = 0
    values = {                                                 # same as before, but with diffrent values
        ('A', 'X'): 3,
        ('A', 'Y'): 4,
        ('A', 'Z'): 8,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 2,
        ('C', 'Y'): 6,
        ('C', 'Z'): 7
    }
    with open(inFile) as f:
        for line in f:
            count += values[(line[0], line[2])]
    return count

print('Solution of part two: ', partTwo(inFile))
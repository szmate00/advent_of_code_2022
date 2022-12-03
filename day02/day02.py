import numpy as np


inFile = "day02/input.txt"

def partOne(inFile: str) -> int:
    count = 0
    with open(inFile) as f:
        for line in f.readlines():
            if line[0] == 'A':
                if line[2] == 'X':
                    count += 4
                elif line[2] == 'Y':
                    count += 8
                else:
                    count += 3
            elif line[0] == 'B':
                if line[2] == 'X':
                    count += 1
                elif line[2] == 'Y':
                    count += 5
                else:
                    count += 9
            elif line[0] == 'C':
                if line[2] == 'X':
                    count += 7 
                elif line[2] == 'Y':
                    count += 2
                else:
                    count += 6
            else:
                pass

    return count

print("Solution of part one: ", partOne(inFile))

def partTwo(inFile: str) -> int:
    count = 0
    with open(inFile) as f:
        for line in f.readlines():
            if line[0] == 'A':
                if line[2] == 'X':
                    count += 3
                elif line[2] == 'Y':
                    count += 4
                else:
                    count += 8
            elif line[0] == 'B':
                if line[2] == 'X':
                    count += 1
                elif line[2] == 'Y':
                    count += 5
                else:
                    count += 9
            elif line[0] == 'C':
                if line[2] == 'X':
                    count += 2 
                elif line[2] == 'Y':
                    count += 6
                else:
                    count += 7
            else:
                pass

    return count

print("Solution of part two: ", partTwo(inFile))
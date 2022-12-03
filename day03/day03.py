import numpy as np


inFile = "day03/input.txt"

def prior(x: str) -> int:
    if x.islower():                                                             # mapping the letter to numbers using by their unicode point
        return ord(x)-96                                                        # 'a' through 'z' have ords 97 through 122
    else:
        return ord(x)-38                                                        # and 'A' through 'Z' have ords 65 through 90

def partOne(inFile: str) -> int:
    count = 0
    with open(inFile) as f:
        for line in f.readlines():                                              # going through each input line
            A = set(char for char in line[:len(line)//2])                       # and separating the two halves into two sets
            B = set(char for char in line[len(line)//2:])
            common = list(A & B)[0]                                             # their intersection will be the common item
            count += prior(common)

    return count

print("Solution of part one: ", partOne(inFile))

def partTwo(inFile: str) -> int:
    count = 0
    with open(inFile) as f:
        lines = []
        for idx, line in enumerate(f.readlines()):                              # almost the same as before
            if (idx+1) % 3 == 0:                                                # but we group every 3 line and find their intersection
                lines.append([*(line.strip('\n'))])
                badge = list(set(lines[0]) & set(lines[1]) & set(lines[2]))[0]
                count += prior(badge)
                lines = []

            else:
                lines.append([*line])

    return count

print("Solution of part two: ", partTwo(inFile))
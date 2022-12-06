import numpy as np
import re


inFile = 'day06/input.txt'
testFile = 'day06/test.txt'

def testFunc1(testFile: str, realSolution: str, part: int) -> None:
    tests = {'mjqjpqmgbljsphdztnvjfqwrcgsmlb': 7,
            'bvwbjplbgvbhsrlpgdmjqwftvncz': 5,
            'nppdvjthqldpwncqszvftbrmjlhg': 6,
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 10,
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 11}
    
    for test in tests:
        mySolution = solveOne(test)
        if mySolution == tests[test]:
            print('TEST PASSED!')
        else:
            print('TEST NOT PASSED')
            print('Your output', mySolution)
            print('Good output', tests[test])
    pass

def readInput(inFile: str) -> str:
    with open(inFile) as f:
        return  f.read()

def solveOne(data: list) -> int:
    data = list(map(str, data))

    for i, elem in enumerate(data):
        if len(data[i:i+4]) == len(set(data[i:i+4])):
            return i+4
        else:
            pass

def partOne(inFile: str) -> int:
    data = readInput(inFile)
    return solveOne(data)              

print('PART 1:')
testFunc1(testFile, 'CMZ', 1)
print('Solution: ', partOne(inFile))
print('')

def testFunc2(testFile: str, realSolution: str, part: int) -> None:
    tests = {'mjqjpqmgbljsphdztnvjfqwrcgsmlb': 19,
            'bvwbjplbgvbhsrlpgdmjqwftvncz': 23,
            'nppdvjthqldpwncqszvftbrmjlhg': 23,
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 29,
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 26}
    
    for test in tests:
        mySolution = solveTwo(test)
        if mySolution == tests[test]:
            print('TEST PASSED!')
        else:
            print('TEST NOT PASSED')
            print('Your output', mySolution)
            print('Good output', tests[test])
    pass

def solveTwo(data: list) -> int:
    data = list(map(str, data))

    for i, elem in enumerate(data):
        if len(data[i:i+14]) == len(set(data[i:i+14])):
            return i+14
        else:
            pass

def partTwo(inFile: str) -> int:
    data = readInput(inFile)
    return solveTwo(data) 

print('PART 2:')
testFunc2(testFile, 'MCD', 2)
print('Solution: ', partTwo(inFile))

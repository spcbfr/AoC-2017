# Author: Yusuf Bouzekri
# solution for Day 2 of Advent of Code 2017
# Link to problem: https://adventofcode.com/2017/day/2

inputLines = open("input.txt", "r").readlines()


def clean(dirtyLine: str):
    # convert a given string into a parsable line
    cleanList = dirtyLine.strip().split("\t")

    # convert every item in the list from a string to an int
    cleanList = [int(item) for item in cleanList]

    return cleanList


fresh = list(map(clean, inputLines))

checksum = 0
for list in fresh:
    min = list[0]
    max = list[0]
    for item in list:
        if item > max:
            max = item
        if item < min:
            min = item
    diff = max - min
    checksum += diff
print(checksum)

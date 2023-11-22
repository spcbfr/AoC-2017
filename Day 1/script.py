# Author: Yusuf Bouzekri
# solution for Day 1 of Advent of Code 2017
# Link to problem: https://adventofcode.com/2017/day/1
import os

cwd = os.getcwd()
print(cwd)

f = open("input.txt", "r")
txt = f.read()


# This will get the proper item of a list
# when given an index, if the given index
# is out-of-range the function will loop
# back and start from the first index
def congruent(index: int, list: list[int]):
    length = len(list)  # 5
    if index < length:
        return list[index]
    else:
        return list[index % length]


count = 0

# Refactored answer for the first half of the question
for index, value in enumerate(txt):
    if congruent(index + 1, txt) == value:
        count += int(value)
print("First Half:", count)


count = 0
midway = int(len(txt) / 2)

for index, value in enumerate(txt):
    if congruent(index + midway, txt) == value:
        count += int(value)

print("Second Half:", count)

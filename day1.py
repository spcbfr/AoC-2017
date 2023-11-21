f = open("input.txt", "r")
txt = f.read()


# This will get the proper item of a list
# when given an index, if the given index
# is out-of-range the function will loop
# back and start from the first index
def doura(index: int, list: list[int]):
    length = len(list)  # 5
    if index < length:
        return list[index]
    else:
        return list[index % length]


count = 0
midway = int(len(txt) / 2)
print(midway)

# Refactored answer for the first half of the question
# for index, value in enumerate(txt):
#     if doura(index + 1, txt) == value:
#         count = count + int(value)


for index, value in enumerate(txt):
    if doura(index + midway, txt) == value:
        count = count + int(value)

print(count)

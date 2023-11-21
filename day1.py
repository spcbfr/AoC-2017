f = open("input.txt", "r")
txt = f.read()

count = 0
for index, value in enumerate(txt):
    if index != len(txt) - 1:
        if txt[index + 1] == value:
            count = count + int(value)
        pass
    else:
        if txt[0] == value:
            count = count + int(value)
print(count)

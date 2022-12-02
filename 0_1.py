m = 0
x = 0
with open("input.txt", "r") as f:
    for line in f:
        if line and line != "\n":
            x += int(line)
        else:
            m = max(min, x)
            x = 0

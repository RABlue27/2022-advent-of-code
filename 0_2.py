m = [0,0,0]
x = 0
with open("input.txt", "r") as f:
    for line in f:
        if line and line != "\n":
            x += int(line)
        else:
            m[0] = max(m[0], x)
            x = 0
            m.sort()

print(sum(m))

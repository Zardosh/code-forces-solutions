y = str(int(input()) + 1)

while len(set(y)) != 4:
    y = str(int(y) + 1)

print(y)
n = input()

events = map(int, input().split())

crimes = 0
cops = 0

for event in events:
    if event == -1:
        if cops > 0:
            cops -= 1
        else:
            crimes += 1
    else:
        cops += event

print(crimes)
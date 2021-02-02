n, h = map(int, input().split())
a = map(int, input().split())

width = 0

for friend in a:
    width += 1 + int(friend > h)

print(width)
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if abs(x - y) > 1:
        moves = x + y + abs(x - y) - 1
    else:
        moves = x + y

    print(moves)
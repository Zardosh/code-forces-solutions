import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    white_cells = math.ceil(n * m // 2)
    black_cells = n * m // 2

    print(white_cells, black_cells)

    if x1 % 2 == y1 % 2:
        white_cells += ((x2 - x1 + 1) * (y2 - y1 + 1)) // 2
        black_cells -= ((x2 - x1 + 1) * (y2 - y1 + 1)) // 2
        print('=1', white_cells, black_cells)
    else:
        white_cells += math.ceil(((x2 - x1 + 1) * (y2 - y1 + 1)) // 2)
        black_cells -= math.ceil(((x2 - x1 + 1) * (y2 - y1 + 1)) // 2)
        print('!=1', white_cells, black_cells)

    if x3 % 2 == y3 % 2:
        black_cells += math.ceil(((x4 - x3 + 1) * (y4 - y3 + 1)) // 2)
        white_cells -= math.ceil(((x4 - x3 + 1) * (y4 - y3 + 1)) // 2)
        print('=2', white_cells, black_cells)
    else:
        black_cells += ((x4 - x3 + 1) * (y4 - y3 + 1)) // 2
        white_cells -= ((x4 - x3 + 1) * (y4 - y3 + 1)) // 2
        print('!=2', white_cells, black_cells)

    print(white_cells, black_cells)



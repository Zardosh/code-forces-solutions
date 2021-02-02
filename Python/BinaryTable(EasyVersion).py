t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    table = [list(input()) for row in range(n)]

    operations = []

    def make_op(x1, y1, x2, y2, x3, y3):
        if table[x1][y1] == '1':
            table[x1][y1] = '0'
        else:
            table[x1][y1] = '1'
            
        if table[x2][y2] == '1':
            table[x2][y2] = '0'
        else:
            table[x2][y2] = '1'
            
        if table[x3][y3] == '1':
            table[x3][y3] = '0'
        else:
            table[x3][y3] = '1'

        operations.append([x1 + 1, y1 + 1, x2 + 1, y2 + 1, x3 + 1, y3 + 1])

    if n != 2:
        for i in range(n - 2):
            for j in range(0, m, 2):
                if j == m - 1:
                    if table[i][j] == '1':
                        make_op(i, j, i + 1, j, i + 1, j - 1)
                else:
                    if table[i][j] == '1':
                        if table[i][j + 1] == '1':
                            make_op(i, j, i, j + 1, i + 1, j + 1)
                        else:
                            make_op(i, j, i + 1, j, i + 1, j + 1)
                    elif table[i][j + 1] == '1':
                        make_op(i, j + 1, i + 1, j, i + 1, j + 1)
    
    if m != 1:
        for i in range(m - 1):
            if table[n - 2][i] == '1':
                if table[n - 1][i] == '1':
                    make_op(n - 2, i, n - 1, i, n - 2, i + 1)
                else:
                    make_op(n - 2, i, n - 2, i + 1, n - 1, i + 1)
            elif table[n - 1][i] == '1':
                make_op(n - 1, i, n - 2, i + 1, n - 1, i + 1)

    square1 = table[n - 2][m - 1] == '1'
    square2 = table[n - 1][m - 1] == '1'

    if square1:
        if square2:
            make_op(n - 2, m - 2, n - 1, m - 2, n - 2, m - 1)
            make_op(n - 2, m - 2, n - 1, m - 2, n - 1, m - 1)
        else:
            make_op(n - 2, m - 1, n - 2, m - 2, n - 1, m - 1)
            make_op(n - 2, m - 2, n - 1, m - 2, n - 2, m - 1)
            make_op(n - 2, m - 1, n - 1, m - 1, n - 1, m - 2)
    elif square2:
        make_op(n - 1, m - 1, n - 2, m - 1, n - 1, m - 2)
        make_op(n - 2, m - 2, n - 1, m - 2, n - 1, m - 1)
        make_op(n - 2, m - 1, n - 2, m - 2, n - 1, m - 1)

    print(len(operations))
    
    for op in operations:
        print(*op)
                    







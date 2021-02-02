t = int(input())

for _ in range(t):
    n = int(input())

    if n // 2 % 2 != 0:
        print('NO')
    else:
        print('YES')

        even = range(2, n + 1, 2)
        odd = list(range(1, n, 2))
        odd[-1] += sum(even) - sum(odd)

        print(*even, *odd)
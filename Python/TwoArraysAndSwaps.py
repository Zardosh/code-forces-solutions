t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for __ in range(k):
        ai = min(a)
        bj = max(b)
        i = a.index(ai)
        j = b.index(bj)

        if ai >= bj:
            break
        else:
            a[i], b[j] = b[j], a[i]

    print(sum(a))
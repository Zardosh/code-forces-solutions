n, l = map(int, input().split())
a = sorted(list(map(int, input().split())))

d = a[0]

for i in range(1, n):
    d = max(d, (a[i] - a[i - 1]) / 2)

d = max(d, l - a[-1])

print(d)

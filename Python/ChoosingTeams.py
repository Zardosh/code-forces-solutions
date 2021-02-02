n, k = map(int, input().split())
y = list(map(int, input().split()))

print(sum([i <= 5 - k for i in y]) // 3)
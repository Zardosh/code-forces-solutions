t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(max(max(a, b), min(a, b) * 2) ** 2)
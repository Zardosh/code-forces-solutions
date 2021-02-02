n = int(input())
p = list(map(int, input().split()))

output = []

for i in range(1, len(p) + 1):
    output.append(p.index(i) + 1)

print(*output)
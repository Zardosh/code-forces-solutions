n, k = map(int, input().split())

problems = 0
time = 0

for i in range(n):
    if 5 * (i + 1) + time > 240 - k:
        break
    else:
        time += 5 * (i + 1)
        problems += 1

print(problems)
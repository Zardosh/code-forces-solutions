n = int(input())

groups = 1
last_magnet = input()

for _ in range(n - 1):
    magnet = input()

    if magnet != last_magnet:
        groups += 1
        last_magnet = magnet

print(groups)
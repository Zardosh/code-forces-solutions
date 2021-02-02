n = int(input())

free_rooms = 0

for _ in range(n):
    p, q = map(int, input().split())

    if p + 2 <= q:
        free_rooms += 1

print(free_rooms)
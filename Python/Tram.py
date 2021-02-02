n = int(input())

min_passengers = 0
cur_passengers = 0

for _ in range(n):
    a, b = map(int, input().split())

    cur_passengers += b - a

    min_passengers = max(cur_passengers, min_passengers)

print(min_passengers)
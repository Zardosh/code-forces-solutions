import math

n, m, a = map(int, input().split())

row = math.ceil(m / a)
column = math.ceil(n / a)

print(row * column)
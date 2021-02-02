k, n, w = map(int, input().split())

total_cost = ((k +  w * k) * w) // 2

print(0 if n > total_cost else total_cost - n)
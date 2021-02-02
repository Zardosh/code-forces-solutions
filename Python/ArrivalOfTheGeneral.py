n = int(input())
a = list(map(int, input().split()))

tallest = max(a)
shortest = min(a)

tallest_index = a.index(tallest)
shortest_index = len(a) - a[::-1].index(shortest) - 1

print(tallest_index + len(a) - shortest_index - 1 - int(shortest_index < tallest_index))

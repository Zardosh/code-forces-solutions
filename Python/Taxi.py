import math

n = int(input())
groups = map(int, input().split())

group_numbers = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

taxis = 0

for group in groups:
    group_numbers[group] += 1

taxis += group_numbers[4]

taxis += group_numbers[3]
group_numbers[1] -= min(group_numbers[3], group_numbers[1])

taxis += group_numbers[2] // 2
group_numbers[2] = group_numbers[2] % 2

taxis += group_numbers[2]
group_numbers[1] -= group_numbers[2] * 2
group_numbers[1] = max(group_numbers[1], 0)

taxis += math.ceil(group_numbers[1] / 4)

print(taxis)

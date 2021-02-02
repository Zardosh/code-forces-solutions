import math

n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

def binary_search(target):
    last_index = n
    current_index = n // 2
    index_difference = -2

    if x[current_index] > target:
        last_index = 0

    print(x)

    while index_difference not in [-1, 0]:
        print(index_difference)
        index_difference = current_index - last_index

        price = x[current_index]
        temp_index = current_index

        if price < target:
            current_index = (current_index + last_index) // 2
        elif price > target:
            current_index = math.ceil((current_index - last_index) / 2)
        else:
            return current_index
            
        last_index = temp_index

    return last_index - index_difference

for _ in range(q):
    print(binary_search(int(input())) + 1)
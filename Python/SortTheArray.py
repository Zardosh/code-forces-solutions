n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)
index_differences = []

for i in range(len(a)):
    if a[i] != sorted_a[i]:
        index_differences.append(i)

if len(index_differences) > 0:
    last_index_difference = index_differences[0]
    is_possible = True
    has_parity_switched = False

    for index_difference in index_differences:
        if not has_parity_switched and index_difference > last_index_difference + 1:
            has_parity_switched = True
        elif index_difference > last_index_difference + 1:
            is_possible = False
            break

        last_index_difference = index_difference

    if is_possible and len(index_differences) % 2 == 0:
        print('yes')
        print(index_differences[0] + 1, index_differences[-1] + 1)
    else:
        print('no')
else:
    print('yes')
    print('1 1')
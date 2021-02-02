m, s = map(int, input().split())

min_number = 10 ** (m - 1)
max_number = min_number * 10 - 1

i = m - 1
digit_sum = 0

if (m == 1 and s == 0):
    print(0, 0)
elif (s < 1 or s > 9 * m):
    print('-1 -1')
else:
    while digit_sum != s:
        digit_sum = sum(map(int, str(min_number)))

        if i == -1:
            print('-1 -1')
            break

        if digit_sum < s - 9:
            temp_number = list(str(min_number))
            temp_number[i] = '9'

            i -= 1

            min_number = int(''.join(temp_number))
        else:
            temp_number = list(str(min_number))
            temp_number[i] = str(s - digit_sum + int(temp_number[i]))

            min_number = int(''.join(temp_number))
            break

    i = m - 1
    digit_sum = 0

    while digit_sum != s:
        digit_sum = sum(map(int, str(max_number)))

        if i == -1:
            print('-1 -1')
            break

        if digit_sum > s + 9:
            temp_number = list(str(max_number))
            temp_number[i] = '0'

            i -= 1

            max_number = int(''.join(temp_number))
        else:
            temp_number = list(str(max_number))
            temp_number[i] = str(int(temp_number[i]) - (digit_sum - s))

            max_number = int(''.join(temp_number))
            break

    print(min_number, max_number)

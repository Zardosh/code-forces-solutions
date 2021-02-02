t = int(input())

for _ in range(t):
    a = int(input())

    if (-360 / (a - 180)).is_integer():
        print('YES')
    else:
        print('NO')
n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print('#' * m)
    else:
        if (i + 1) % 4 == 0:
            print('#' + '.' * (m - 1)) 
        else:
            print('.' * (m - 1) + '#')
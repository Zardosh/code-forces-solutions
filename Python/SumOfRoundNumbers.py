t = int(input())

for _ in range(t):
    n = input()

    print(len(n) - n.count('0'))

    for i in range(len(n)):
        if n[i] != '0':
            print(n[i] + '0' * (len(n) - i - 1), end=' ')

    print()
n = int(input())

x = 0

for _ in range(n):
    statement = input()

    if '++' in statement.split('X'):
        x += 1
    else:
        x -= 1

print(x)
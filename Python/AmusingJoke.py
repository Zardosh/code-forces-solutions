g1 = input()
g2 = input()
letters = input()

if sorted(g1 + g2) == sorted(letters):
    print('YES')
else:
    print('NO')
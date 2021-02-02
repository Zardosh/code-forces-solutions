n = int(input())
s = input().lower()

output = 'YES'

for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter not in s:
        output = 'NO'
        break

print(output)
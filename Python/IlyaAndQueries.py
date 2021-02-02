s = input()
m = int(input())

sequences = []
value = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        value += 1

    sequences.append(value)

print(sequences, s)

for _ in range(m):
    l, r = map(int, input().split())

    if r - l > 1:
        print(sequences[r - 2] - sequences[l - 1])
    else:
        print(sequences[l - 1] - sequences[l - 2])

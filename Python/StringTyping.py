n = int(input())
s = input()

word = ''
biggest_repetition = 1

for i in range(len(s)):
    word += s[i]

    if word in s[i + 1:i + len(word) + 1]:
        biggest_repetition = max(biggest_repetition, len(word))

print(len(s) - biggest_repetition + 1)
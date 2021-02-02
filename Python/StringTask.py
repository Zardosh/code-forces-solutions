word = input()

final_word = ''

for char in word:
    if char.lower() not in 'aiueoy':
        final_word += '.' + char.lower()

print(final_word)
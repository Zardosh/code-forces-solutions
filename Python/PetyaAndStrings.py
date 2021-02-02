first_word = input().lower()
second_word = input().lower()

output = 0

for i in range(len(first_word)):
    if ord(first_word[i]) > ord(second_word[i]):
        output = 1
        break
    elif ord(first_word[i]) < ord(second_word[i]):
        output = -1
        break
        
print(output)
n = input()
money = map(int, input().split())

biggest_sequence = 0
current_sequence = 0
last_number = 0

for i in money:
    if i >= last_number:
        current_sequence += 1
    else:
        biggest_sequence = max(biggest_sequence, current_sequence)
        current_sequence = 1
    
    last_number = i

biggest_sequence = max(biggest_sequence, current_sequence)

print(biggest_sequence)

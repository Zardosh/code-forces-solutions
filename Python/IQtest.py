n = int(input())
numbers = list(map(int, input().split()))

odd_numbers = []
even_numbers = []

for i in range(n):
    if numbers[i] % 2 == 0:
        even_numbers.append(i + 1)
    else:
        odd_numbers.append(i + 1)

if len(even_numbers) == 1:
    print(even_numbers[0])
else:
    print(odd_numbers[0])


        
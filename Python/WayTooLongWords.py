n = int(input())

for _ in range(n):
    word = input()

    print(word if len(word) <= 10 else word[0] + str(len(word) - 2) + word[-1])

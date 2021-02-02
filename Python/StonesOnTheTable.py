n = int(input())
stones = input()

last_stone = ''
answer = 0

for stone in stones:
    if last_stone == stone:
        answer += 1

    last_stone = stone

print(answer)
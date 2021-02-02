n, k = map(int, input().split())
participants = list(map(int, input().split()))

target_score = participants[k - 1]

total = 0

for participant in participants:
    if participant >= target_score and participant > 0:
        total += 1

print(total)
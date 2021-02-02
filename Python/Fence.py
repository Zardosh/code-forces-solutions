n, k = map(int, input().split())
h = list(map(int, input().split()))

smallest_segment = 1
smallest_sum = 99999999999999999999999

for i in range(n - k):
    segment_sum = sum(h[i:i + k])

    if segment_sum < smallest_sum:
        smallest_sum = segment_sum
        smallest_segment = i + 1

print(smallest_segment)
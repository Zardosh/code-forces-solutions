n = int(input())
shows = [list(map(int, input().split())) for _ in range(n)]

shows.sort(key=lambda x: x[0])

tv1 = [-1, -1]
tv2 = [-1, -1]

output = 'YES'

for show in shows:
    if show[0] > tv1[1]:
        tv1 = show
    elif show[0] > tv2[1]:
        tv2 = show
    else:
        output = 'NO'
        break

print(output)
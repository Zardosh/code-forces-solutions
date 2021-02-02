n = int(input())
px = list(map(int, input().split()))
py = list(map(int, input().split()))

x = px[1:]
y = py[1:]

x.extend(y)

if len(set(x)) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
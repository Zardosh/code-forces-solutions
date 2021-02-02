t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    output = 'YES'
    last = a[0]

    for i in a:
        if not i <= last + 1:
            output = 'NO'
            break
        
        last = i

    print(output)
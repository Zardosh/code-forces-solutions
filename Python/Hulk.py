n = int(input())

feelings = [['I hate', 'I love'][int(i % 2)] for i in range(n)]

print(' that '.join(feelings) + ' it')
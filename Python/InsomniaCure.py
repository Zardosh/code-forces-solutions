k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

kdamage = list(range(k - 1, d, k))
ldamage = list(range(l - 1, d, l))
mdamage = list(range(m - 1, d, m))
ndamage = list(range(n - 1, d, n))

ndamage.extend(kdamage)
ndamage.extend(ldamage)
ndamage.extend(mdamage)

print(len(set(ndamage)))
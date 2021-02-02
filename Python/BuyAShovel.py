k, r = map(int, input().split())

shovels = 1
price = k

while str(price)[-1] not in ['0', str(r)]:
    price += k
    shovels += 1

print(shovels)
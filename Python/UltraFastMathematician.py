n1 = input()
n2 = input()

print(bin(int(n1, 2) ^ int(n2, 2))[2:].zfill(len(str(n1))))
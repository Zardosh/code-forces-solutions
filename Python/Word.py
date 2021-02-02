s = input()

lc_count = 0
uc_count = 0

for c in s:
    if c.islower():
        lc_count += 1
    else:
        uc_count += 1

print(s.lower() if lc_count >= uc_count else s.upper())
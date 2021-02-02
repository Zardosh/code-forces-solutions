s = input()

if s == '{}':
    print(0)
else:
    s = s.strip('}{').split(', ')
    print(len(set(s)))


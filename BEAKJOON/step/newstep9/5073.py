while True:
    t = list(map(int, input().split()))
    t.sort()

    if t[0] == 0 and t[1] == 0 and t[2] == 0:
        break

    if t[0] + t[1] <= t[2]:
        print('Invalid')
    elif t[0] == t[1] and t[1] == t[2] and t[0] == t[2]:
        print('Equilateral')
    elif t[0] == t[1] or t[1] == t[2] or t[0] == t[2]:
        print('Isosceles')
    elif t[0] != t[1] and t[1] != t[2] and t[0] != t[2]:
        print('Scalene')

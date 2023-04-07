N = int(input())
plan = list(map(str, input().split()))
a, b = 1, 1

for i in plan:
    if i == 'L' and b > 1:
        b -= 1
    elif i == 'R' and b < N:
        b += 1
    elif i == 'U' and a > 1:
        a -= 1
    elif i == 'D' and a < N:
        a += 1

print(a, b)
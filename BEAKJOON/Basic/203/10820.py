import sys
input = sys.stdin.readline

while True:
    lower, upper, num, space = 0, 0, 0, 0
    S = input().strip('\n')

    if not S:
        break

    for i in S:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        elif i == ' ':
            space += 1
    print(lower, upper, num, space)
import sys
input = sys.stdin.readline

n = int(input())

a = []
b = 1
result = []
flag = 0
for i in range(n):
    num = int(input())

    while b <= num:
        a.append(b)
        result.append('+')
        b += 1
    
    if a[-1] == num:
        a.pop()
        result.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for j in result:
        print(j)
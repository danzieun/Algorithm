import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

b = []
for i in a:
    b.append(max(i))

max_num = 0
for i in b:
    max_num = max(b)

print(max_num)

for i in range(9):
    for j in range(9):
        if a[i][j] == max_num:
            print(i+1, j+1, end=' ')

import sys

a = [[0]*100 for _ in range(100)]

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            a[k][j] = 1

w = 0
for i in a:
    w += sum(i)

print(w)

import sys

N, M = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


c = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        c[i][j] = a[i][j] + b[i][j]

for i in c:
    for j in i:
        print(j, end=' ')
    print()
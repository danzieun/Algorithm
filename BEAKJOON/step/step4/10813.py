import sys

N, M = map(int, sys.stdin.readline().split())

a = []
for i in range(N):
    a.append(i+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

print(*a)
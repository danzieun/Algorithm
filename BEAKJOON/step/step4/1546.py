import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
top = max(a)

for i in range(N):
    a[i] = a[i]/top*100

print(sum(a)/N)
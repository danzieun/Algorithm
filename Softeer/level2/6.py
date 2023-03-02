import sys

N = int(sys.stdin.readline())

a = 2
for i in range(N):
    a += pow(2, i)

print(pow(a, 2))
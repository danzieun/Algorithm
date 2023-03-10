import sys

N = int(input())

a = [int(sys.stdin.readline()) for _ in range(N)]

a.sort()

for i in a:
    print(i)
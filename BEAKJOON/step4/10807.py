import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(a.count(v))
import sys

a = []
for _ in range(10):
    n = int(sys.stdin.readline())
    a.append(n % 42)

a = set(a)
print(len(a))
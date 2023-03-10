import sys

a = [int(sys.stdin.readline()) for _ in range(5)]
a.sort()

print(sum(a)//5)
print(a[2])
import sys

num = [i for i in range(1, 31)]

for _ in range(28):
    n = int(sys.stdin.readline())
    num.remove(n)

print(min(num))
print(max(num))
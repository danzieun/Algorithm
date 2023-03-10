import sys

N = int(sys.stdin.readline())
num = str(sys.stdin.readline())

sum = 0
for i in range(N):
    sum += int(num[i])

print(sum)
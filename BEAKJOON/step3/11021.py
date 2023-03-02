import sys

T = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for i in range(T):
    print('Case #%d:' %(i+1), a[i][0] + a[i][1])
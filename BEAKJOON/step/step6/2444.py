import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    print(' '*(N-i), '*'*(2*i-1), sep='')
for i in range(N+1, 2*N):
    print(' '*(i-N), '*'*(2*(2*N-i)-1), sep='')
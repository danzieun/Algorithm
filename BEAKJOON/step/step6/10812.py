import sys

N, M = map(int, sys.stdin.readline().split())

N_list = [i for i in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    N_list[i-1:j] = N_list[k-1:j] + N_list[i-1:k-1]

print(*N_list)
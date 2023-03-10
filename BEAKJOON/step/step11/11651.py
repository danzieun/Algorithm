import sys
input = sys.stdin.readline

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]

N_list = sorted(N_list, key = lambda x : (x[1], x[0]))

for i in range(N):
    print(N_list[i][0], N_list[i][1])
X = int(input())
N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]

sum = 0
for i in range(N):
    sum += N_list[i][0] * N_list[i][1]

if X == sum:
    print('Yes')
else:
    print('No')
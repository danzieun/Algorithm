import sys

M, N, K = map(int, sys.stdin.readline().split())
M_list = ''.join(list(map(str, sys.stdin.readline().split())))
N_list = ''.join(list(map(str, sys.stdin.readline().split())))

if M_list in N_list:
    print('secret')
else:
    print('normal')
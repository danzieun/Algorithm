# 코드트리 빵

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
store = [list(map(int, input().split())) for _ in range(m)]

time = 0

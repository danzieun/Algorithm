# 주사위 굴리기

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
map_list = [list(map(int, input().split)) for _ in range(n)]
k_list = list(map(int, input().split()))
dice = [[-1, 0, -1], [0, 0, 0], [-1, 0, -1], [-1, 0, -1]]


import sys

N = int(sys.stdin.readline())   # 입력으로 주어진 방

n = 1   # 벌집 수
cnt = 1 # 최소 개수의 방
while N > n:
    n += 6 * cnt
    cnt += 1

print(cnt)
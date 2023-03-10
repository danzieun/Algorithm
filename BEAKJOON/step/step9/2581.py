import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

a = []  # 소수인지 확인하기 위해 임시로 만든 배열
b = []  # 소수 배열
for i in range(M, N+1):
    # 소수 확인 부분
    if i > 1:
        for j in range(1, int(i ** 1/2) + 1):
            if i % j == 0:
                a.append(j)

        if len(a) == 1:
            b.append(i)
        else:
            pass
        a = []

# 소수가 있으면 합과 최솟값 출력, 아니면 -1 출력
if len(b) != 0:
    print(sum(b))
    print(min(b))
else:
    print(-1)
# [S/W 문제해결 기본] 1일차 - View

for num in range(1, 11):
    n = int(input())
    n_list = list(map(int, input().split()))
    cnt = 0

    for i in range(2, n-2):
        a = n_list[i] - n_list[i-2]
        b = n_list[i] - n_list[i-1]
        c = n_list[i] - n_list[i+1]
        d = n_list[i] - n_list[i+2]

        if a > 0 and b > 0 and c > 0 and d > 0:
            cnt += min(a, b, c, d)

    print('#%d' %num, cnt)

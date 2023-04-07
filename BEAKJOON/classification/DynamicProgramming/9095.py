# 1, 2, 3 더하기

t = int(input())

for _ in range(t):
    n = int(input())
    n_list = [0] * (n+3)

    n_list[1] = 1
    n_list[2] = 2
    n_list[3] = 4

    for i in range(4, n+1):
        n_list[i] = n_list[i-1] + n_list[i-2] + n_list[i-3]
    
    print(n_list[n])
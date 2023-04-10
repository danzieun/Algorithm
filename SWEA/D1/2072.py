# 2072. 홀수만 더하기

t = int(input())

for num in range(1, t+1):
    t_list = list(map(int, input().split()))
    result = 0

    for i in t_list:
        if i % 2 == 1:
            result += i
    
    print('#%d' %num, result)

T = int(input())

for _ in range(T):
    S = input().split()
    
    for i in S:
        if i != S[-1]:
            print(i[::-1], end=' ')
        else:
            print(i[::-1])
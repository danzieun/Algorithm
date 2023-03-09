import sys
input = sys.stdin.readline

N = int(input())
X_list = list(map(int, input().split()))

X_set = set(X_list)
X_set = sorted(X_set)

dic = {X_set[i]:i for i in range(len(X_set))}

for i in X_list:
    print(dic[i], end=' ')
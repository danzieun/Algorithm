from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
result = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
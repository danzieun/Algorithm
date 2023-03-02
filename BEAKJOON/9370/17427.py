N = int(input())
f = []

for i in range(1, N+1):
    for j in range(1, i//2+1):
        if i % j == 0:
            f.append(j)
    f.append(i)

print(sum(f))
'''
N = input()

a = []
sum = 0
for i in range(int(N)):
    sum += i
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    
    if sum == int(N):
        a.append(i)
    sum = 0

if len(a) == 0:
    print(0)
else:
    print(min(a))
'''

N = int(input())

for i in range(N+1):
    N_sum = i + sum(map(int, str(i)))
    
    if N_sum == N:
        print(i)
        break
    elif i == N:
        print(0)
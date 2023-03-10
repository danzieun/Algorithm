import sys

N = int(sys.stdin.readline())

cnt = 0
for _ in range(N):
    a = sys.stdin.readline().strip()
    if list(a) == sorted(a, key=a.find):
        cnt += 1

print(cnt)

'''
b = []
for _ in range(N):
    a = list(sys.stdin.readline().strip())
    
    for i in range(len(a)):
        if i != len(a)-1:
            if a[i] == a[i+1]:
                pass
            else:
                b.append(a[i])
        else:
            b.append(a[i])
        
    if len(b) == len(set(b)):
        cnt += 1
    b = []

print(cnt)
'''

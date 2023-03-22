import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = []
c = len(s1)
M = int(input())

for _ in range(M):
    a = input().strip().split()

    if a[0] == 'L' and s1 != []:
        s2.append(s1.pop())        
    if a[0] == 'D' and s2 != []:
        s1.append(s2.pop())
    if a[0] == 'B' and s1 != []:
        s1.pop()
    if a[0] == 'P':
        s1.append(a[1])

print(''.join(s1 + list(reversed(s2))))
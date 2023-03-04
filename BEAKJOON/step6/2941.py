import sys

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = sys.stdin.readline().strip()

for i in a:
    if i in s:
        s = s.replace(i, '*')

print(len(s))
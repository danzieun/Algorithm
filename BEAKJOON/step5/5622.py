import sys

S = sys.stdin.readline().strip()

num = ['ABC',
       'DEF',
       'GHI',
       'JKL',
       'MNO',
       'PQRS',
       'TUV',
       'WXYZ']

time = 0
for i in S:
    for j in num:
        if i in j:
            time += num.index(j) + 3

print(time)
import sys

a = [sys.stdin.readline().strip() for _ in range(5)]
s = ''

for i in range(15):
    for j in range(5):
        if len(a[j]) > i:
            s += a[j][i]

print(s)

'''
length = []
for i in a:
    length.append(len(i))
max_length = max(length)

for i in range(5):
    if len(a[i]) < max_length:
        a[i] += ' '*(max_length-len(a[i]))

s = []
for i in range(max_length):
    for j in range(5):
        if a[j][i] == ' ':
            pass
        else:
            s.append(a[j][i])

print(''.join(s))
'''
import sys

num = {'0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    'x': '0000000'}

def length(string):
    if len(string) == 5:
        return string
    else:
        return (5-len(string))*'x' + string

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = length(a)
    b = length(b)

    cnt = 0
    for i in range(5):
        for j in range(7):
            if num[a[i]][j] != num[b[i]][j]:
                cnt += 1
    print(cnt)
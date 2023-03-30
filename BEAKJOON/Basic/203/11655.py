S = input()
nS = ''

for i in S:
    if i.isupper():
        n = ord(i) + 13
        while n > 90:
            n -= 26
        nS += chr(n)
    elif i.islower():
        n = ord(i) + 13
        while n > 122:
            n -= 26
        nS += chr(n)
    else:
        nS += i

print(nS)
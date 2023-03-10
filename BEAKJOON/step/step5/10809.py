S = input()

for i in range(97, 123):
    print(S.find(chr(i)), end=' ')

'''
a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
'''
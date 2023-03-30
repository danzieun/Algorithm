S = list(input())
result = [''.join(S)]

for _ in range(len(S)-1):
    S.pop(0)
    result.append(''.join(S))

result.sort()

for i in result:
    print(i)
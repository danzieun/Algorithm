s = list(input())

answer = 0
result = []
for i in range(len(s)):
    if s[i] == '(':
        result.append('(')
    elif s[i] == ')':
        if s[i-1] == '(':
            result.pop()
            answer += len(result)
        else:
            result.pop()
            answer += 1

print(answer)
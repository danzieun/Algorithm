S = list(input().strip())

tag = False
result = ''
stack = ''
for i in S:
    if tag == False:
        if i == '<':
            tag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        else:
            stack = i + stack
    elif tag == True:
        stack += i
        if i == '>':
            tag = False
            result += stack
            stack = ''

print(result + stack)
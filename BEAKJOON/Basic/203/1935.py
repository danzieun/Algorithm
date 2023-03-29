import sys
input = sys.stdin.readline

N = int(input())
A = input().strip()

for i in range(N):
    A = A.replace(chr(65+i), input().strip())

stack = []
for i in range(len(A)):
    if A[i].isdigit():
        stack.append(A[i])
    else:
        a = float(stack.pop())
        b = float(stack.pop())
        if A[i] == '+':
            stack.append(b + a)
        elif A[i] == '-':
            stack.append(b - a)
        elif A[i] == '*':
            stack.append(b * a)
        elif A[i] == '/':
            stack.append(b / a)

print('%.2f' %stack[0])
import sys
input = sys.stdin.readline

N = int(input())
N_list = []

def push(a):
    N_list.append(a)

def pop():
    if len(N_list) == 0:
        print(-1)
    else:
        N_pop = N_list.pop()
        print(N_pop)

def size():
    print(len(N_list))

def empty():
    if len(N_list) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(N_list) != 0:
        print(N_list[-1])
    elif len(N_list) == 0:
        print(-1)

for _ in range(N):
    a = input().split()

    if a[0] == 'push':
        push(a[1])
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'size':
        size()
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'top':
        top()
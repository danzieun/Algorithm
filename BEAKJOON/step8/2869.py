import sys

A, B, V = map(int, sys.stdin.readline().split())

'''
state = 0
day = 1
while V > state:
    state += A
    if V <= state:
        break
    state -= B
    day += 1

print(day)
'''

A-B 
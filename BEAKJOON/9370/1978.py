""" N = input()
N_list = list(map(int, input().split()))
a = []

for i in N_list:   
    if i == 1:
        continue
    elif i == 2:
        a.append(i)
    for j in (2, int(i**0.5)+1):
        if i % j == 0:
            break
        else:
            a.append(i)
            break

print(a)
print(len(a)) """

import math

N = input()
N_list = list(map(int, input().split()))

for i in N_list:
    array = [True for j in range(i+1)]
    for k in range(2, int(math.sqrt(i))+1):
        if array[k] == True:
            m = 2
            while k * m <= i:
                array[k * m] = False
                m += 1

print(array)
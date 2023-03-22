a = int(input())
b = int(input())
c = int(input())

if a == 60 & b == 60 & c == 60:
    print('Equilateral')
elif a+b+c == 180:
    if a == b or a == c or b == c:
        print('Isosceles')
    elif a != b and a != c and b != c:
        print('Scalene')
else:
    print('Error')
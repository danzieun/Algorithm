import sys

max_value = 0
max_location = 0

for i in range(9):
    a = int(sys.stdin.readline())
    max_value = max(max_value, a)
    if max_value == a:
        max_location = i + 1

print(max_value)
print(max_location)
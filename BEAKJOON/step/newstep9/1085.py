x, y, w, h = list(map(int, input().split()))

print(min(w-x, h-y, x-0, y-0))
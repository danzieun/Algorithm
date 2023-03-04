import sys
from collections import Counter

s = sys.stdin.readline().strip()
s = s.upper()

cnt = Counter(s)
cnt = cnt.most_common()

if len(s) != 1:
    if cnt[0][1] == cnt[1][1]:
        print('?')
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
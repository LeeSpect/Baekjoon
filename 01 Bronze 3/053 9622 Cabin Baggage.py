# 053 9622 Cabin Baggage.py

import sys

t = int(sys.stdin.readline())
cnt = 0
for _ in range(t):
    l,wi,d,we = map(float, sys.stdin.readline().split())
    if (l > 56 and wi > 45 and d > 25) or sum([l,wi,d]) > 125 or we > 7:
        print(0)
    else:
        print(1)
        cnt += 1
print(cnt)        

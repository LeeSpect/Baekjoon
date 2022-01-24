# 053 9622 Cabin Baggage.py

# 틀린 
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


# 수정 코드 : ((l > 56 or wi > 45 or d > 25) and l+wi+d > 125) or we > 7 : if 문의 조건을 잘 확인하지 못했음.

import sys

t = int(sys.stdin.readline())
cnt = 0
for _ in range(t):
    l,wi,d,we = map(float, sys.stdin.readline().split())
    if ((l > 56 or wi > 45 or d > 25) and l+wi+d > 125) or we > 7:
        print(0)
    else:
        print(1)
        cnt += 1
print(cnt)       

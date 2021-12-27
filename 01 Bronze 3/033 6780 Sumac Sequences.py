# 033 6780 Sumac Sequences.py

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

cnt = 2
while 1:
    a = a-b
    if a < 0: break
    else:
        cnt += 1
        b = b-a
        if b < 0: break
        else:
            cnt += 1
print(cnt)
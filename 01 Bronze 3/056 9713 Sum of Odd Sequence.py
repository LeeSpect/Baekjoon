# 056 9713 Sum of Odd Sequence.py

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    total = 0
    n = int(sys.stdin.readline())
    for i in range(1,n+1,2):
        total += i
    print(total)

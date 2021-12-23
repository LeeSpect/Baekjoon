# 024 5612 터널의 입구와 출구.py

import sys

n = int(sys.stdin.readline())
s0 = int(sys.stdin.readline())
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    s0 += (a-b)
print(s0)
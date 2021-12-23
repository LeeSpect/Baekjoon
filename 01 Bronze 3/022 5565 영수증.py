# 022 5565 영수증.py

import sys

n = int(sys.stdin.readline())
for _ in range(9):
    s = int(sys.stdin.readline())
    n -= s
print(n)
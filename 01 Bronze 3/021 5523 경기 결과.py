# 021 5523 경기 결과.py

import sys

n = int(sys.stdin.readline())
a_point = 0; b_point = 0
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    if a == b:
        continue
    elif a > b: a_point += 1
    else: b_point += 1
print(a_point, b_point)
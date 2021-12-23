# 023 5607 問題 １.py

import sys

t = int(sys.stdin.readline())
a_score = 0; b_score = 0
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    if a == b:
        a_score += a
        b_score += b
    elif a > b:
        a_score += a+b
    else:
        b_score += a+b
print(a_score, b_score)
# 025 5613 계산기 프로그램.py

import sys

score = int(sys.stdin.readline())
while True:
    a = str(sys.stdin.readline().rstrip())
    if a == '=':
        print(score)
        break
    else:
        b = int(sys.stdin.readline())
        if a == '+':
            score += b
        elif a == '-':
            score -= b
        elif a == '*':
            score *= b
        else:
            score //= b

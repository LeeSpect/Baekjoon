# 030 6609 모기곱셈.py

import sys

while 1:
    try:
        m,p,l,e,r,s,n = map(int, sys.stdin.readline().split())
        for i in range(n):
            m,p,l = p//s, l//r, m*e
        print(m)
    except ValueError:
        break
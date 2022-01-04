# 052 9610 사분면.py

import sys

T = int(sys.stdin.readline())
q1,q2,q3,q4,ax = 0,0,0,0,0
for _ in range(T):
    x,y = map(int, sys.stdin.readline().split())
    if x==0 or y==0:
        ax += 1
    elif x>0 and y>0:
        q1 += 1
    elif x<0 and y>0:
        q2 += 1
    elif x<0 and y<0:
        q3 += 1
    else:
        q4 += 1
print('Q1: '+f'{q1}')
print('Q2: '+f'{q2}')
print('Q3: '+f'{q3}')
print('Q4: '+f'{q4}')
print('AXIS: '+f'{ax}')

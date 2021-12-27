# 028 6437 Golf.py

import sys

cnt = 1
while 1:
    a,b = map(int, sys.stdin.readline().split())
    if a==b==0: break
    print(f'Hole #{cnt}')

    if b == 1: print('Hole-in-one.')
    elif a-b > 2: print('Double eagle.')
    elif a-b == 2: print('Eagle.')
    elif a-b == 1: print('Birdie.')
    elif a-b == 0: print('Par.')
    elif a-b == -1: print('Bogey.')
    elif a-b <= -2: print('Double Bogey.')

    cnt += 1
    print()
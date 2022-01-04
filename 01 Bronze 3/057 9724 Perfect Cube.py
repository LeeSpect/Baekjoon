# 057 9724 Perfect Cube.py

import sys

t = int(sys.stdin.readline())
for _ in range(1,t+1):
    a,b = map(int, sys.stdin.readline().split())
    cnt = 0
    for i in range(1260):
        x = i**3
        if x < a: continue
        elif x > b: break
        else:
            cnt += 1
    print(f'Case #{_}'+': '+f'{cnt}')


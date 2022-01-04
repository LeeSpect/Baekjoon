# 055 9699 RICE SACK.py

import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    l = list(map(int, sys.stdin.readline().split()))
    print(f'Case #{i}'+': '+f'{max(l)}')

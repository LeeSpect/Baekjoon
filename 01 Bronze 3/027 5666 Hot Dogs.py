# 027 5666 Hot Dogs.py

import sys
try:
    while True:
        a,b = list(map(int, sys.stdin.readline().split()))
        print(f'{a/b:.2f}')
except ValueError:
    pass
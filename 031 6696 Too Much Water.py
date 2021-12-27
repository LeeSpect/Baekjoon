# 031 6696 Too Much Water.py

import sys
PIE = 3.141592653589793238

while 1:
    a,b = map(float, sys.stdin.readline().split())
    if a==b==0: break
    i = int(((a**2+b**2)*PIE+99)//100)
    print(f'The property will be flooded in hour {i}.')

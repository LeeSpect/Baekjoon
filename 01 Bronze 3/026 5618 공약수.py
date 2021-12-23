# 026 5618 공약수.py

import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
for i in range(1, l[n-1]):
    if n == 2:
        if l[0]%i == 0 and l[1]%i == 0:
            print(i)
    else:
        if l[0]%i == 0 and l[1]%i == 0 and l[2]%i == 0:
            print(i)
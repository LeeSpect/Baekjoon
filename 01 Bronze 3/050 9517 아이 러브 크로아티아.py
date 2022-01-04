# 050 9517 아이 러브 크로아티아.py

import sys

K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sec = 210
for _ in range(N):
    t,z = map(str, sys.stdin.readline().split())
    sec -= int(t)
    if sec <= 0: break
    if z == 'T':
        K += 1
        if K == 9: K=1
print(K)

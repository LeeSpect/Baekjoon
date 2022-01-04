# 051 9550 아이들은 사탕을 좋아해.py

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N,K = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        l[i] //= K
    print(sum(l))

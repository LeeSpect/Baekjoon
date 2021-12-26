# 026 5618 공약수.py (틀린 코드)

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
            
# 026 5618 공약수.py (수정 코드)
# 수정 코드 : gcd 함수 사용

from math import gcd


n = int(input())
l = list(map(int, input().split()))
l.sort()
g = gcd(l[0], l[1])
for i in range(1, n):
    new_g = gcd(g, l[i])    
for _ in range(1,new_g+1):
    if new_g%_ == 0:
        print(_)

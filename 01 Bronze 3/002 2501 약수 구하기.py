# 002 2501 약수 구하기.py

n,k = map(int, input().split())
c = 0

for i in range(1, n+1):
    if n%i == 0:
        c += 1
        if c == k:
            print(i)
if k > c: print(0)
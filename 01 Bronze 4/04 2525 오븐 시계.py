# 04 2525 오븐 시계.py

A,B = map(int, input().split())
C = int(input())

print((A+(B+C)//60)%24, (B+C)%60)
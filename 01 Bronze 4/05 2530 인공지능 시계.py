# 05 2530 인공지능 시계.py

A,B,C = map(int, input().split())
D = int(input())
print((A+(B+(C+D)//60)//60)%24, (B+(C+D)//60)%60, (C+D)%60)
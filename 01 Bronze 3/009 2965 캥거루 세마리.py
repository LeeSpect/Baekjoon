# 009 2965 캥거루 세마리.py

a,b,c = map(int, input().split())
if b-a > c-a:
    print(b-a-1)
else:
    print(c-b-1)
import sys; input=sys.stdin.readline

t=int(input())
for _ in range(t):
    a,b,s=map(int,input().split())
    if (s%2 and a==0) or (a+b*2<s):
        print('NO')
    else:
        print('YES')

import sys; input=sys.stdin.readline

t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if c in [a+b,a-b,b-a,a*b,a/b,b/a]:
        print('Possible')
    else:
        print('Impossible')

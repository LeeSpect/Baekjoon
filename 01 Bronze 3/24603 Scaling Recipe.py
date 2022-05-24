import sys; input=sys.stdin.readline

n,x,y=map(int,input().split())
for i in range(n):
    k=int(input())
    print(int(k/x*y))

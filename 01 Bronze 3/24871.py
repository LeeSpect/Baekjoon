import sys; input=sys.stdin.readline

d,m,w=map(int,input().split())
i,j,k=map(int,input().split())
ans=(k-1)*m*d+(j-1)*d+i-1

print(chr(97+ans%w))

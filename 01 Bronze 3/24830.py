import sys; input=sys.stdin.readline

t=int(input())
cash=1
for i in range(t):
    a,b,c=map(str,input().split())
    if b=='+':
        cash=int(a)+int(c)-cash
    elif b=='-':
        cash=(int(a)-int(c))*cash
    elif b=='*':
        cash=(int(a)*int(c))**2
    else:
        if int(a)%2==0:
            cash=int(a)//2
        else:
            cash=(int(a)+1)//2
    print(cash)

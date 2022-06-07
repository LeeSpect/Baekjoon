import sys; input=sys.stdin.readline

t=int(input())
for i in range(1,t+1):
    r,a,b=map(int,input().split())
    ans=0
    pos='r'
    while r!=0:
        if pos=='r':
            if ans!=0:
                r//=b
            ans+=r*r*3.1415926535
            pos='l'
        else:
            r*=a
            ans+=r*r*3.1415926535
            pos='r'

    print(f'Case #{i}: {ans:0.6f}')

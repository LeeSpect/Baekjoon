import sys; input=sys.stdin.readline

t=int(input())
for _ in range(t):
    s,f,k=map(str,input().split())
    sh=3600*int(s[:2])+60*int(s[3:5])+int(s[6:])
    fh=3600*int(f[:2])+60*int(f[3:5])+int(f[6:])
    if sh>=fh:
        sh=86400-sh
        time=fh+sh
    else:
        time=fh-sh
    k=int(k)*60
    if k<=time:
        print('Perfect')
    elif k<=time+3600:
        print('Test')
    else:
        print('Fail')

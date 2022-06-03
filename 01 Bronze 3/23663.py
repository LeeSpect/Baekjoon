import sys; input=sys.stdin.readline

t=int(input())
for _ in range(t):
    red,white=map(int,input().split())
    red_list=list(map(int,input().split()))
    white_list=list(map(int,input().split()))
    if red<=white:
        print('Yes')
    else:
        print('No')

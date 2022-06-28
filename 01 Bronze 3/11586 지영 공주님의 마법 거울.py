import sys; input=sys.stdin.readline

def main():
    t=int(input())
    l=[]
    for _ in range(t):
        l.append(input().rstrip())
    k=int(input())
    if k==1:
        for i in range(t):
            print(l[i])
    elif k==2:
        for i in range(t):
            print(l[i][::-1])
    else:
        for i in range(t-1,-1,-1):
            print(l[i])

if __name__=='__main__':
    main()

import sys; input=sys.stdin.readline

def main():
    cnt=1
    while 1:
        n,d=map(int,input().split())
        if n==d==0:
            break
        Becs,Cas=[i for i in range(n)],[i for i in range(n)]
        B=int(input())
        if B:
            Becs.pop(B-1)
        C=int(input())
        if C:
            Cas.pop(-C)

        print(f'Scenario {cnt}')
        for i in range(1,d+1):
            a,b=map(int,input().split())
            print(f'Day {i}', end=' ')
            if Becs[a-1]==Cas[-b]:
                print('ALERT')
            else:
                print('OK')
        cnt+=1

if __name__=='__main__':
    main()

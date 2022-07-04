import sys; input=sys.stdin.readline

def main():
    n=int(input())
    l=list(map(str,input().split()))
    cnt=0
    for word in l:
        if word in ['he','him','she','her']:
            cnt+=1
    print(cnt)

if __name__=='__main__':
    main()

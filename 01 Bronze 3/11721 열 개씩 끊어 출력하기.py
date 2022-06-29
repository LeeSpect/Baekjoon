import sys; input=sys.stdin.readline

def main():
    string=input().rstrip()
    n=len(string)
    for i in range(n):
        print(string[i],end='')
        if (i+1)%10==0:
            print()

if __name__=='__main__':
    main()

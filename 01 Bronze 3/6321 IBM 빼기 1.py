import sys; input=sys.stdin.readline

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZA'

def main():
    t=int(input())
    for i in range(t):
        k=input().rstrip()
        ans=''
        for j in range(len(k)):
            ans+=alphabet[alphabet.index(k[j])+1]
        print(f'String #{i+1}')
        print(ans)
        print()

if __name__=='__main__':
    main()

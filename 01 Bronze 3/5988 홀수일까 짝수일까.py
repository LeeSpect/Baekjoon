import sys; input=sys.stdin.readline

def main():
    t=int(input())
    for i in range(t):
        if int(input())%2==0:
            print('even')
        else:
            print('odd')

if __name__=='__main__':
    main()

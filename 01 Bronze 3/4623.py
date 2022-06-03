while True:
    a,b,c,d = map(int, input().split())
    if a==b==c==d==0: break
    else:
        if bool(a-b >= 0) == bool(c-d >= 0):
            if a<=c and b<=d:
                print('100%')
            else:
                if int(c/a*100) < int(d/b*100):
                    print(f'{int(c/a*100)}%')
                else: print(f'{int(d/b*100)}%')
        else:
            if a<=d and b<=c:
                print('100%')
            else:
                if int(d/a*100) < int(c/b*100):
                    print(f'{int(d/a*100)}%')
                else: print(f'{int(c/b*100)}%')
            

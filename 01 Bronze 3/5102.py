while True:
    a,b = map(int, input().split())
    if a==b==0: break
    else:
        if (a-b)%2 == 0:
            aa = (a-b)//2
            bb = 0
        elif a-b == 0 or a-b == 1:
            print('0 0')
            continue
        else:
            aa = (a-b-3)//2
            bb = 1
        print(aa, bb)
            
            

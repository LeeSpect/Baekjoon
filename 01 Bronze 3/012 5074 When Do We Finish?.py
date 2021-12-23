# 012 5074 When Do We Finish?.py

while True:
    x,y = map(str, input().split())
    if x == '00:00' and y == '00:00': break
    else:    
        a,b = map(int, x.split(':'))
        c,d = map(int, y.split(':'))
        
        n = 0
        h = a + c
        if b + d >= 60:
            h += 1
            m = (b+d)%60
        else:
            m = b+d
        if h >= 24:
            n += h//24
            h = h%24
        
        # 출력문
        if n == 0:
            print(f'{h:0>2}:{m:0>2}')
        else:
            print(f'{h:0>2}:{m:0>2} +{n}')

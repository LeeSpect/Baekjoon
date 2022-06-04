while True:
    l = list(map(int, input().split()))
    if sum(l) == 0: break
    else:
        l.sort()
        if l[2] >= l[0] + l[1]:
            print('Invalid')
        elif l[0]==l[1]==l[2]:
            print('Equilateral')
        elif l[0]==l[1] or l[0]==l[2] or l[1]==l[2]:
            print('Isosceles')
        else:
            print('Scalene')
    

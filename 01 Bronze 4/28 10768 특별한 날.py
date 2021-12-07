# 28 10768 특별한 날.py 3:38

m = int(input())
d = int(input())
if m - 2 < 0:
    print('Before')
elif m -2 > 0:
    print('After')
else:
    if d - 18 < 0:
        print('Before')
    elif d - 18 > 0:
        print('After')
    else:
        print('Special')
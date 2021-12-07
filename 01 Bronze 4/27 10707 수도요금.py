# 27 10707 수도요금.py 24.53 6.88

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

if p <= c:
    if a*p <= b:
        print(a*p)
    else:
        print(b)
else:
    if a*p <= b+d*(p-c):
        print(a*p)
    else:
        print(b+d*(p-c))
# 054 9664 NASLJEDSTVO.py
# 틀린 
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if (b*a/(a-1))%2 == 0:
    print(int(b*a/(a-1))-1, int(b*a/(a-1)))
else:
    print(int(b*a/(a-1)), int(b*a/(a-1)))

    
# 수정 코드
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if b/(a-1)%1==0:
    print(b//(a-1)-1+b, b//(a-1)+b)
else:
    print(b//(a-1)+b, b//(a-1)+b)

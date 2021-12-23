# 020 5361 전투 드로이드 가격.py

t = int(input())
for _ in range(t):
    a,b,c,d,e = map(int, input().split())
    print(f'${a*350.34 + b*230.9 + c*190.55 + d*125.3 + e*180.9:.2f}')
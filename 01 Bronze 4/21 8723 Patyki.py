# 21 8723 Patyki.py

L = list(map(int, input().split()))
m = L.pop(L.index(max(L)))
if sum(L) > m:
    print(1)
else:
    print(0)
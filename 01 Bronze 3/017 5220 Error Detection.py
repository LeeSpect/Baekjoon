# 017 5220 Error Detection.py

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    a16 = bin(a)[2:]
    cnt = 0
    for i in range(len(a16)):
        if int(a16[i])%2 != 0:
            cnt += 1
    if (cnt%2 == 0 and b==0) or (cnt%2 == 1 and b==1):
        print('Valid')
    else: print('Corrupt')
# 004 2511 카드놀이.py

la = list(map(int, input().split()))
lb = list(map(int, input().split()))
ap, bp = 0, 0
s = ''

for i in range(10):
    if la[i] > lb[i]:
        ap += 3
        s = 'A'
    elif la[i] < lb[i]:
        bp += 3
        s = 'B'
    else:
        ap += 1
        bp += 1
print(ap, bp)
if ap > bp: print('A')
elif ap < bp: print('B')
elif s == 'A': print('A')
elif s == 'B': print('B')
else: print('D')

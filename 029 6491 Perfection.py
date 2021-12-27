# 029 6491 Perfection.py     

import sys

def get_D(n):
    data = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            data.append(i)
            if i**2 != n:
                data.append(n//i)
    return data


l = list(map(int, sys.stdin.readline().split()))
ll = len(l)
for i in range(ll):
    if l[i] == 0: break
    data = get_D(l[i])
    s = sum(data)
    if s-l[i] == l[i]: print(f'{l[i]} PERFECT')
    elif s-l[i] > l[i]: print(f'{l[i]} ABUNDANT')
    else: print(f'{l[i]} DEFICIENT')
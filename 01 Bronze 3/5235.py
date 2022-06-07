import sys

n = int(input())
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))[1:]
    odd_cnt = 0; even_count = 0
    for i in range(len(l)):
        if l[i]%2 == 0: even_count += l[i]
        else: odd_cnt += l[i]
    if odd_cnt > even_count:
        print('ODD')
    elif odd_cnt < even_count:
        print('EVEN')
    else:
        print('TIE')
        

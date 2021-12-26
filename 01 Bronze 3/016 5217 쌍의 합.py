# 016 5217 쌍의 합.py

n = int(input())
for _ in range(n):
    k = int(input())
    data = []

    for i in range(1, k//2+1):
        if k-i != i:
            data.append([i, k-i])
    print(f'Pairs for {k}: ', end ='')
    for i in range(len(data)):
        if i == len(data)-1:
            print(data[i][0], data[i][1], end = '')
        else:
            print(data[i][0], data[i][1], end = ', ')
    print()

m = 0; idx = 0; row = 0
for i in range(9):
    l1 = list(map(int, input().split()))
    if max(l1) > m:
        m = max(l1)
        idx = l1.index(max(l1))+1
        row = i+1
print(m)
print(row, idx)

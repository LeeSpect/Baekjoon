Lmin = list(map(int, input().split()))
Lman = list(map(int, input().split()))

if sum(Lmin) > sum(Lman):
    print(sum(Lmin))
else:
    print(sum(Lman))

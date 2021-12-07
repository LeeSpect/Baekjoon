# 12 5596 시험 점수.py

Lmin = list(map(int, input().split()))
Lman = list(map(int, input().split()))

if sum(Lmin) > sum(Lman):
    print(sum(Lmin))
else:
    print(sum(Lman))
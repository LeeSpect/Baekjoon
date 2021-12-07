# 22 10039 평균 점수.py

L = [int(input()) for i in range(5)]
for i in range(len(L)):
    if L[i] < 40:
        L[i] = 40
print(sum(L)//len(L))
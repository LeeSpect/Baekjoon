# 005 2547 사탕 선생 고창영.py

n = int(input())

for _ in range(n):
    space = input()
    n_students = int(input())
    l_st = []
    for __ in range(n_students):
        l_st.append(int(input()))
    if sum(l_st)%n_students == 0: print('YES')
    else: print('NO')
    
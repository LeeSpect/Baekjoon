# 019 5354 J박스.py

n = int(input())
for _ in range(n):
    j = int(input())
    print('#'*j)
    for i in range(j-2):
        print('#'+'J'*(j-2)+'#')
    print('#'*j)
    if _ != n-1:
        print()
# 019 5354 J박스.py (틀린 코드)

n = int(input())
for _ in range(n):
    j = int(input())
    print('#'*j)
    for i in range(j-2):
        print('#'+'J'*(j-2)+'#')
    print('#'*j)
    if _ != n-1:
        print()
        
        
# 019 5354 J박스.py (수정 코드 :  J가 1일때를 생각하지 못했음)

n = int(input())
for _ in range(n):
    j = int(input())
    if j == 1:
        print('#')
        if _ != n-1:
            print()
    else:
        print('#'*j)
        for i in range(j-2):
            print('#'+'J'*(j-2)+'#')
        print('#'*j)
        if _ != n-1:
            print()

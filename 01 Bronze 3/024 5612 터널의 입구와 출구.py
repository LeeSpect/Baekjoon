# 024 5612 터널의 입구와 출구.py (틀린 코드)

import sys

n = int(sys.stdin.readline())
s0 = int(sys.stdin.readline())
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    s0 += (a-b)
print(s0)


# 024 5612 터널의 입구와 출구.py (수정코드)
# 수정코드 : 가장 높은 최대값, 0 이하로 내려가면 음수 구현

import sys

n = int(sys.stdin.readline())
s0 = int(sys.stdin.readline())
memory = s0
con = 1
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    s0 += (a-b)
    if s0 < 0:
        con = 0
    if s0 > memory:
        memory = s0
if con == 0: print(0)
else: print(memory)

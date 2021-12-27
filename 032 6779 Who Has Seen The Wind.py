# 032 6779 Who Has Seen The Wind.py

import sys

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())
con = 0
for t in range(1, m+1):
    a = t*(-6*t**3 + h*t**2 + 2*t + 1)
    if a <= 0:
        con = t
        break

if con == 0:
    print('The balloon does not touch ground in the given time.')
else:
    print(f'The balloon first touches ground at hour: {con}')
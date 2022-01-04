# 054 9664 NASLJEDSTVO.py

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if (b*a/(a-1))%2 == 0:
    print(int(b*a/(a-1))-1, int(b*a/(a-1)))
else:
    print(int(b*a/(a-1)), int(b*a/(a-1)))

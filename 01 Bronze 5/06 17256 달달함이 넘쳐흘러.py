# 06 17256 달달함이 넘쳐흘러.py

ax,ay,az = map(int, input().split())
cx,cy,cz = map(int, input().split())

print(cx-az, int(cy/ay), cz-ax)
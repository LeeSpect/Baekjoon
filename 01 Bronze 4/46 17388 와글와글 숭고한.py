# 46 17388 와글와글 숭고한.py

l = list(map(int, input().split()))
if sum(l) >= 100:
    print('OK')
elif min(l) == l[0]:
    print('Soongsil')
elif min(l) == l[1]:
    print('Korea')
else:
    print('Hanyang')

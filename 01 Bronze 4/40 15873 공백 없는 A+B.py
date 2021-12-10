# 40 15873 공백 없는 A+B.py

s = input()
if len(s) == 2:
    print(int(s[0]) + int(s[1]))
elif s[:2] == s[2:] == '10':
    print(20)
elif s[:2] == '10':
    print(int(s[:2]) + int(s[-1]))
else:
    print(int(s[0]) + int(s[1:]))

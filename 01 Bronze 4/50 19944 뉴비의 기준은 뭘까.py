# 50 19944 뉴비의 기준은 뭘까.py

n,m = map(int, input().split())
print(m<=2 and 'NEWBIE!' or m<=n and 'OLDBIE!' or 'TLE!')
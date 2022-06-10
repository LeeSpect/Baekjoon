import sys; input=sys.stdin.readline
from math import hypot

def main():
    h1,m1,s1=map(int,input().split(':'))
    h2,m2,s2=map(int,input().split(':'))
    
    t1=s1+m1*60+h1*3600
    t2=s2+m2*60+h2*3600
    
    if t1==t2:
        print('24:00:00')
        exit()
    elif h1>h2 or (h1>=h2 and m1>m2) or (h1>=h2 and m1>=m2 and s1>s2):
        t1=3600*24-t1
        t=t1+t2
    else:
        t=t2-t1
    
    print(f'{t//3600:02d}:{(t-t//3600*3600)//60:02d}:{t%60:02d}')
                        
if __name__=='__main__':
    main()

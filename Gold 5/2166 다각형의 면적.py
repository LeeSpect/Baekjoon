# 틀린 코드: abs 함수를 잘못된 위치에 놓았다.
import sys; input=sys.stdin.readline

def main():
    N=int(input())
    dots=[tuple(map(int,input().split())) for _ in range(N)]
    area=0
    x1,y1=dots[0]
    for i in range(1,N-1):
        x2,y2=dots[i]; x3,y3=dots[i+1]
        area+=0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1))
    print(f'{area:0.1f}')

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# 수정 코드: abs함수와 *0.5를 뒤로 빼서, 출력 직전에 적용되도록 하였다.
import sys; input=sys.stdin.readline

def main():
    N=int(input())
    dots=[tuple(map(int,input().split())) for _ in range(N)]
    area=0
    x1,y1=dots[0]
    for i in range(1,N-1):
        x2,y2=dots[i]; x3,y3=dots[i+1]
        area+=(x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1)
    print(f'{abs(area)*0.5:0.1f}')

if __name__=='__main__':
    main()

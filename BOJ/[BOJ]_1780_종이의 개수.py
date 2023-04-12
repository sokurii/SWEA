'''
같은 수로만 되어 있다면 종이 그대로 사용
그게 아니라면 종이를 9개로 나눈 뒤 잘린 종이에 대해 반복
-1로만, 0으로만, 1로만 채워진 종이 개수 세기
'''
import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
minus,zero,plus = 0,0,0

def divide(r,c,N):
    paper = arr[r][c]
    global minus,zero,plus

    for i in range(r,r+N):
        for j in range(c,c+N):
            if arr[i][j] != paper:
                area = N//3

                divide(r,c,area)
                divide(r,c+area,area)
                divide(r,c+2*area,area)

                divide(r+area,c,area)
                divide(r+area,c+area,area)
                divide(r+area,c+2*area,area)

                divide(r+2*area,c,area)
                divide(r+2*area,c+area,area)
                divide(r+2*area,c+2*area,area)

                return

    if paper == -1:
        minus += 1
    elif paper == 0:
        zero += 1
    else:
        plus += 1

divide(0,0,N)
print(minus)
print(zero)
print(plus)

'''
2630, 1992번과 다르게 시간 많이 소요됐다.

분할정복 알고리즘도 응용하기가 쉽다
비슷한 문제 많이 풀면서 익히기 바람! 
'''
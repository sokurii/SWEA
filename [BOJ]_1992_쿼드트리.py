'''
다른 글자가 있으면 괄호 열고 4분할 탐색
탐색 마치면 괄호 닫기
'''

N = int(input())
arr = [list(input()) for _ in range(N)]
result = ''

def divide(r,c,N):
    global result
    square = arr[r][c]

    for i in range(r,r+N):
        for j in range(c,c+N):
            if arr[i][j] != square:
                # 다르니까 열린 괄호로 시작
                result += '('

                # 탐색 범위 1/2로 줄여서 재귀
                half = N//2
                divide(r,c,half)
                divide(r,c+half,half)
                divide(r+half,c,half)
                divide(r+half,c+half,half)

                # 마쳤으면 닫힌 괄호
                result += ')'
                return

    if square == '1':
        result += '1'
    else:
        result += '0'


divide(0,0,N)
print(result)


'''
return에 대하여..
return은 함수 자체를 빠져나감(def divide)
계속 재귀를 도니까 그 전에 실행했던 divide함수로 돌아가는 것 
'''
'''
색이 모두 같은 경우가 아니면 4분할 후 재귀
색이 모두 같은 경우라면 해당 색 개수 세기
* 분할정복 알고리즘 익숙하지 않아서 풀이 보면서 공부함
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def divide(r, c, N):
    global white, blue
    color = arr[r][c]

    for i in range(r, r+N):
        for j in range(c, c+N):
            if color != arr[i][j]:
                half = N//2
                divide(r, c, half)
                divide(r, c+half, half)
                divide(r+half, c, half)
                divide(r+half, c+half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

divide(0,0,N)
print(white)
print(blue)



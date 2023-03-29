T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    box = [[0]*N for _ in range(N)]

    # 시작점 채우기
    box[0][0] = arr[0][0]
    for i in range(N):
        for j in range(N):
            if 0<i<=N and 0<j<=N:
                # 맨 위, 맨 왼쪽 행과 열 채우기
                box[0][j] = arr[0][j] + box[0][j-1]
                box[i][0] = arr[i][0] + box[i-1][0]
                # 나머지 공간 채우기
                box[i][j] = arr[i][j] + min(box[i-1][j], box[i][j-1])


    ans = box[N-1][N-1]

    print(f'#{tc} {ans}')
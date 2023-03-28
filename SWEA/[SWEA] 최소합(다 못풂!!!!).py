T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    box = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            box[0][0] = arr[0][0]

            if 0<i<=N and 0<j<=N:
                box[i][j] =
                # box[0][j] = arr[0][j]  + box[0][j-1]
                # box[i][0] = arr[i][0] + box[i-1][0]
    print(box)
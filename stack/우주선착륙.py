T = int(input())
dx = [-1,-1,-1,0,0,1,1,1] # 8방향에 대한 델타 값
dy = [-1,0,1,-1,1,-1,0,1]

for tc in range(1,T+1):
    n,m = map(int,input().split())
    ground = [list(map(int,input().split())) for _ in range(n)]
    ans = 0

    for x in range(n):
        for y in range(m):
            cnt = 0
            for k in range(8):
                nx,ny = x + dx[k],y+dy[k]
                if 0 <= nx < n and 0<= ny < m:
                    if ground[x][y] > ground[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                ans += 1
    print(f'#{tc} {ans}')
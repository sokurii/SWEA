'''
1. NxM 공간에 상하좌우 각각 K칸씩 터지는 폭탄
2. 벽(#)을 만나면 폭탄(@) 차단(유의성 설정 시)
3. 빈칸(_)에 폭발된 곳은 '%'로 출력

'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N,M = map(int,input().split())
K = int(input())
ground = [list(input()) for _ in range(N)]


for r in range(N):
    for c in range(M):
        if ground[r][c] == '@':
            ground[r][c] = '%'

            for k in range(4):
                for l in range(1,K+1):
                    nr, nc = r + dr[k]*l, c + dc[k]*l  #폭탄의 범위만큼 위치 설정
                    if 0 <= nr < N and 0 <= nc < M and ground[nr][nc] == '#':
                        break
                    elif 0 <= nr < N and 0 <= nc < M and ground[nr][nc] == '_':
                        ground[nr][nc] = '%'

for ans in ground:
    print(*ans,sep='')



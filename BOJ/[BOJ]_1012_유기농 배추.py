'''
1. MxN 배열에 K개 배추 위치(X,Y)를 저장한다
2. 배열을 순회하면서 값이 1인 길의 거리를 계산한다
3. 거리를 계산한 값들을 새로운 리스트에 넣어준다
4. 리스트 길이 = 필요한 최소 지렁이 수
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc):

    q = []
    q.append((sr,sc))

    while q:
        r, c = q.pop(0)

        for k in range(4):
            nr, nc = r + dr[k], c+dc[k]

            if 0<=nr<N and 0<=nc<M and ground[nr][nc] == 1:
                q.append((nr,nc))
                ground[nr][nc] = ground[r][c] + 1

    return 1 # 반복문을 벗어나면 지렁이 있는 곳 탐색 완료


T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())
    ground = [[0]*M for _ in range(N)]

    for _ in range(K):
        X,Y = map(int,input().split())
        ground[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                cnt += bfs(i,j)

    print(cnt)


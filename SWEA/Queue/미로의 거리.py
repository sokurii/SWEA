dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc): # 출발점의 행, 열
    # 초기화
    visited = [[0]*N for _ in range(N)] # 방문행렬 생성
    q = []              # 큐 생성
    q.append((sr,sc))   # 출발점의 행, 열을 큐에 삽입
    visited[sr][sc] = 1 # 출발점 방문처리


    # 큐가 비어 있다면 모두 탐색한 것으로 인식
    # 큐가 빌 때 까지 반복
    while q:
        r,c = q.pop(0)  # 큐의 맨 앞 원소 꺼내기

        if maze[r][c] == 3:
            return visited[r][c] - 2
            break

        # r,c 기준 델타 탐색
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            # 다음 위치가 유효한 지 검사
            # 2차원 범위 내 & 벽이 아님 & 방문한 적 없음
            if 0<=nr<N and 0<=nc<N:
                if maze[nr][nc] != 1:
                    if not visited[nr][nc]:
                        q.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + 1

    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    # 현재 위치
    r, c = 0, 0

    # 출발점(2) 열과 행
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j

    print(f'#{tc} {bfs(r, c)}')

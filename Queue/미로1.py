# 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(100)]

    # 출발점 설정
    r, c = 0, 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                r,c = i,j

    # BFS
    # 초기값 설정 (방문배열, 큐, 큐에 출발점 삽입, 출발점 방문처리)
    visited = [[0] * 100 for _ in range(100)]
    q = []
    q.append((r,c))
    visited[r][c] = 1

    # 기본값으로 0(도착 못함) 설정. 중간에 도착점 만나면 바꿔줄 것
    road = 0

    # 큐가 빌 때 까지 탐색 반복
    # 만약 비어있다면 탐색 완료
    while q:
        r, c = q.pop(0)

        # 만약 도착점을 만났다면 탈출 성공
        if maze[r][c] == 3:
            road = 1
            break

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            # 2차원 배열 범위 안 & 벽이 아님 & 방문한 적 없음
            if 0<=nr<100 and 0<=nc<100 and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = 1

    print(f'#{tc} {road}')






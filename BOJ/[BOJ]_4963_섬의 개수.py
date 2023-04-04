'''
가로, 세로, 대각선으로 연결되어 있으면 하나의 섬 => 델타
배열이 0과 1로만 이루어져있어서 방문배열을 따로 만들지 않았다.
'''

dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]

def bfs(r,c):
    q = [(r,c)]         # 큐에 넣어주고
    graph[r][c] = 0     # 방문처리(원래는 visited)

    # 큐가 빌 때까지 반복
    while q:
        sr, sc = q.pop(0)
        # 상하좌우,대각선 델타 탐색
        for k in range(8):
            nr,nc = sr+dr[k], sc+dc[k]
            if 0<=nr<h and 0<=nc<w and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                q.append((nr,nc))
    return 1    # 탐색 완료 후 1 반환 - - > cnt += 1


while True:
    w, h = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(h)]

    # 종료조건
    if w==0 and h==0:
        break

    cnt = 0
    # 현재 위치
    for i in range(h):
        for j in range(w):
            # 값이 1일 때(섬) bfs
            if graph[i][j] == 1:
                cnt += bfs(i,j)
    print(cnt)












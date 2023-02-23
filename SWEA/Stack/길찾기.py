def dfs(s):
    # 방문배열
    visited = [0] * 100
    # 스택 생성
    stack = []
    # 출발지점 방문 처리
    i = s
    visited[i] = 1 # 방문

    # 스택 빌 때 까지 반복
    while True:

        if i == 99: # 현재 위치가 도착지점이면
            return 1 # 출발점에서 도착점으로 잘 갔으므로 1 

        for w in range(100):
            if adj[i][w] == 1 and visited[w] == 0: # 인접행렬에 간선이 존재하고, 방문한 적 없으면
                visited[w] = 1 # 방문
                stack.append(i) # 출발지점 스택에 저장
                i = w # 방문한 w를 다시 출발지점으로
                break # 현재위치 탐색 중단, 다음위치로 이동

        else: # 현재 위치 i에서 방문할 수 있는 w가 없으면
            if stack: # 스택에 뭐가 남아 있으면
                i = stack.pop() # 이전 지점으로 
            else: # 스택이 비어있으면 방문 종료
                break
    return 0 # 길 없으므로 0 

T = 10
for tc in range(1,T+1):
    t, E = map(int,input().split()) # 테케, 간선 개수
    edges = list(map(int,input().split()))

    # 인접행렬 생성
    adj = [[0]*100 for _ in range(100)]

    for i in range(E):
        adj[edges[i*2]][edges[i*2+1]] = 1  # 연결된 노드를 인접행렬에 표시

    print(f'#{tc} {dfs(0)}')

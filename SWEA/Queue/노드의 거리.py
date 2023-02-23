def bfs(adj,s,n): # 인접리스트, 시작노드, 노드 개수
    # 초기화
    visited = [0]*(n+1) # 1. 방문배열 생성
    q = []              # 2. 큐 생성
    q.append(s)         # 3. 출발점 큐에 저장
    # visited[s] = 1    # 4. 출발점 방문체크

    # 큐가 비어 있다면 모두 탐색한 것으로 인식
    # 큐가 빌 때 까지 반복
    while q:
        t =q.pop(0)         # 큐의 맨 앞 원소 꺼내오기
        for nt in adj[t]:   # 현 위치와 연결된 모든 노드 탐색
            if not visited[nt]:
                q.append(nt)
                visited[nt] = visited[t]+1

    return visited[G]



T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # 노드와 간선
    adj = [[] for _ in range(V+1)] # 인접 리스트
    for _ in range(E):
        start, to = map(int,input().split())
        adj[start].append(to)
        adj[to].append(start)

    S,G = map(int,input().split())

    bfs(adj,S,V)

    print(f'#{tc} {bfs(adj,S,V)}')


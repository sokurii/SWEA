def dfs(V,S):
    visited = [0] * (V+1)
    stack = []
    stack.append(S) # 출발점 

    while stack: # 스택에 뭔가 있으면
        s = stack.pop() # 제거
        visited[s] = 1  # 방문표시

        for e in range(V+1): # 방문한 적 없고 인접행렬에 간선 있으면
            if visited[e] == 0 and adj[s][e] == 1:
                stack.append(e) # 스택에 이동지점 저장
    return(visited[G])

# import pprint

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # 노드랑 간선 개수
    adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬 생성
    for _ in range(E):
        edges = list(map(int,input().split()))
        adj[edges[0]][edges[1]] = 1 # 인접행렬에 간선 표시 (연결돼있다)
    # pprint.pprint(adj)
    S, G = map(int,input().split()) # 출발점 도착점

    print(f'#{tc} {dfs(V,S)}')
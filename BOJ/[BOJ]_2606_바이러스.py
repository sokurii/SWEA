'''
1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수
1번 노드 방문했을때의 깊이. . cnt로 세주기
'''

# 노드에 방문해서(인접행렬의 요소에 있으면서)
# 방문하지 않았다면 방문체크 후 cnt +1
# 방문한 노드에 대해 또 dfs 재귀
def dfs(v):
    global cnt
    for i in adj[v]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(i)

V = int(input())
E = int(input())

# 인접행렬 만들고, 양방향 표시
adj = [[] for _ in range(V+1)]
for _ in range(E):
    start,end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

# 방문배열 만들고, 출발점 방문표시
visited = [0 for _ in range(V+1)]
visited[1] = 1
cnt = 0
dfs(1)

print(cnt)
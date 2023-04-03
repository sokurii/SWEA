n = int(input())
start,to = map(int,input().split())
m = int(input())

# 인접 리스트
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split()) # x:부모 ,y:자식
    adj[x].append(y)
    adj[y].append(x)

# 방문 리스트
visited = [0] * (n+1)

# 촌수 계산
def dfs(s):
    # 인접 요소 탐색
    for i in adj[s]:
        if not visited[i]:
            visited[i] = visited[s] + 1
            dfs(i)

dfs(start)

if visited[to] == 0:
    print(-1)
else:
    print(visited[to])


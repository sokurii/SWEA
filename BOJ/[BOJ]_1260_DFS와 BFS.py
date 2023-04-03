'''
DFS와 BFS탐색 결과를 출력
단 방문 가능 정점이 여러개일 때 작은 것부터 방문(오름차순)
정점 번호는 1번 ~ V번
정점 개수 V, 간선 개수 E, 탐색 시작할 정점 번호 S
'''

def dfs(s):
    visited1[s] = 1
    # 인접리스트에 있고, 방문하지 않았으면 dfs
    for i in adj[s]:
        if not visited1[i]:
            dfs_lst.append(i) # 출력할 리스트에 방문 노드 추가
            dfs(i)

def bfs(s):
    visited2[s] = 1
    q = [s]
    while q:
        t = q.pop(0)
        for i in adj[t]:
            if not visited2[i]:
                visited2[i] = 1
                bfs_lst.append(i)
                q.append(i)


V,E,S = map(int,input().split())

# 인접행렬
adj = [[] for _ in range(V+1)]
for _ in range(E):
    start,to = map(int,input().split())
    adj[start].append(to)
    adj[to].append(start)

# 배열 속 리스트 오름차순 정렬
for lst in adj:
    lst.sort()

# 방문배열
visited1 = [0] * (V+1)  # dfs
visited2 = [0] * (V+1)  # bfs

# [1] DFS
dfs_lst = [S]
dfs(S)
print(*dfs_lst)

# [2] BFS
# 방문배열, 방문체크
bfs_lst = [S]
bfs(S)
print(*bfs_lst)


'''
def DFS(s):
    visited1[s] = 1
    print(node, end=' ')    # 출력을 이렇게 하는 방법도 있다. 
    
    for next in a[node]:   
        if not chk[next]:   
            DFS(next)       
'''
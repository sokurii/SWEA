'''
1. N개의 정점과 M개 간선 무방향 그래프
2. 정점번호는 1~N번 => N+1 리스트 만들기
3. 정점 R에서 출발한 방문 순서 출력
** 인접 정점은 오름차순으로 방문한다 **

=> 인접리스트 요소를 오름차순 정렬 하는 과정을 생각하지 못했다(심지어 다른 테케 틀림)
=> 계속 틀렸다고 채점돼서 왜 틀렸는 지 궁금함
=> pop(0)인데 pop()을 써서 오답이 나오는 거였다. .
'''
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[R] = 1
q = [R]
cnt = 1

for _ in range(M):
    start, to = map(int,input().split())
    adj[start].append(to)
    adj[to].append(start)

for i in range(1,N+1):
    adj[i].sort()

while q:
    t = q.pop(0)
    for nt in adj[t]:
        if not visited[nt]:
            cnt += 1
            visited[nt] = cnt
            q.append(nt)

for k in visited[1:]:
    print(k)








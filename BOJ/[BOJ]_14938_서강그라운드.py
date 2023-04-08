'''
[다익스트라]
- 하나의 정점 1 -> 모든 정점 N
- 매번 가장 적은 비용의 노드를 하나씩 선택하는 로직

[플로이드 워셜]
- 모든 정점 N -> 모든 정점 N
- 애초에 거치는 정점을 하나씩 다 설정해 직접 확인
- 즉, 거치는 정점을 기준으로 최단 거리 계산
'''
n, m, r = map(int,input().split())  # m : 수색범위
item = [0]+list(map(int,input().split())) # 정점별 아이템 수
INF = 1e8
distance = [[INF]*(n+1) for _ in range(n+1)] # 길의 길이

# 인접한 간선 간의 길이 정보 추가
for _ in range(r):
    a, b, l = map(int,input().split())
    distance[a][b] = l
    distance[b][a] = l

# 자기 자신은 거리 값 없음(정점 번호 1~)
for i in range(1,n+1):
    distance[i][i] = 0

# *플로이드 워셜 핵심
# 바로 가는 것(i->j)과 거쳐 가는 것(i->k + k->j) 중 빠른 길 저장하며 거리값 갱신
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

# 획득가능한 최대 아이템 수
mx = 0
for s in range(1,n+1):  # 출발점
    cnt = 0
    for e in range(1,n+1):  # 현재 위치도 포함해서 계산
        if distance[s][e] <= m:
            cnt += item[e]
    mx = max(mx,cnt)

print(mx)









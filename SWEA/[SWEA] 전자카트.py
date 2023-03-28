'''
- 출발지는 1, 1로 복귀
=> 방문처리 해주고 시작
- n = 방문한 구역 수
- ans = 하나당 최대 10개, 비용은 100이하의 자연수이므로 최대비용 * N
'''

# dfs(방문한 도시 개수(이미1에서 시작했으니 1), 배터리 소모량, 현재 출발점 도시)
def dfs(n,sm,cur):
    global ans

    # *가지치기: 조건에 부합하면 그 다음은 안봐도 되니까 return
    if ans<=sm:
        return

    if n == N:
        # 여태까지의 배터리 소모량 + 현위치에서 1번으로 복귀 비용
        ans = min(ans, sm+arr[cur][1])
        return

    for i in range(2,N+1):
        if v[i] == 0:
            v[i] = 1    # 방문표시
            dfs(n+1, sm+arr[cur][i], i) # dfs(2군데 방문, 0+arr[cur][2], 현재 위치는 2)
            v[i] = 0    # 초기화


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 문제 그대로 인덱스 쓰기 위해 0으로 여분의 공간 만들어준 배열
    arr = [[0]*(N+1)] +[[0] + list(map(int,input().split())) for _ in range(N)]

    ans = 100*N         # 최대비용 * N
    v = [0] * (N+1)     # 방문배열 생성

    dfs(1, 0, 1)
    print(f'#{tc} {ans}')



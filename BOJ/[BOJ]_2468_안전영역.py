'''
- 영역의 개수 : 네 방향, 범위 내, 미방문 > h
- 높이의 최대값만큼 반복, 높이별로 안전영역 개수 구해서 최대값 도출
- ans = 0. h(0~99) 바꾸면서 최대값 구하기

=> max(map(max,arr)) 배열에서 최대값 추출하는 방법을 알게 되었음
=> 런타임 에러 (RecursionError)
   python에서 재귀 depth = 3000
   N <= 100 이므로 depth는 10000을 훨씬 넘는다.
    => import sys
       sys.setrecursionlimit(100000)
'''
import sys
sys.setrecursionlimit(100000)

def dfs(si,sj,h):
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        # 범위 내, 높이>h, 미방문
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]>h and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni,nj,h)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0



# 배열의 최대값 만큼 반복
for h in range(max(map(max,arr))):

    # 높이 바뀔때마다 초기화 (cnt, 방문배열)
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    # 배열 탐색
    for i in range(N):
        for j in range(N):
            # 높이 > h, 미방문
            if arr[i][j]>h and not visited[i][j]:
                visited[i][j] = 1 # 방문처리
                cnt += 1 # 안전영역 개수 +1
                dfs(i,j,h)
    ans = max(ans,cnt)

print(ans)





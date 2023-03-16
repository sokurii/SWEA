'''
- 배열은 0과 1로만 되어 있으므로 방문배열을 만들지 않고, 방문하면 0으로 바꿔주기
- 배열의 상하좌우를 탐색하여 1이 있으면 DFS 탐색, cnt +=1
- cnt 초기화 해주며 결과값을 ans 리스트에 저장
=> DFS로 풀었는데 DFS, BFS 중 무슨 기준으로 풀 방법을 선택하는 지 모르겠다..!
'''

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
ans = []
cnt = 0

def dfs(si,sj):
    global cnt
    arr[si][sj] = 0
    cnt+=1

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]== 1:
            dfs(ni,nj)


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i,j)
            ans.append(cnt)


print(len(ans))

ans.sort()
for a in ans:
    print(a)

